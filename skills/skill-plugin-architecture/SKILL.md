---
name: skill-plugin-architecture
description: Microkernel and extensible plugin system design patterns (dynamic discovery, uniform lifecycle hooks, sandboxing, error boundaries, rate limiting). Use when designing or extending modular toolkits, CLI plugins, data ingestion pipelines, or multi-engine frameworks.
---

# Plugin Architecture Skill

This skill provides architectural patterns and implementation standards for designing modular, extensible systems where tools, integrations, and data sources can be added as self-contained plugins without modifying core orchestrator code.

---

## 1. The Microkernel / Plugin Architecture Pattern

A robust plugin system decouples the **Core Orchestrator** from individual **Plugin Implementations**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          Core Plugin Orchestrator                           │
│  - Plugin Registry & Dynamic Discovery (entry_points / filesystem scan)    │
│  - Lifecycle Hooks Orchestration                                           │
│  - Error Boundaries, Timeouts, Rate Limiting & Concurrency Control          │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ Implements BasePlugin Contract
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
┌───────────────┐              ┌───────────────┐              ┌───────────────┐
│ Tool Plugin A │              │ Tool Plugin B │              │ Tool Plugin C │
│ - Validation  │              │ - Validation  │              │ - Validation  │
│ - Execution   │              │ - Execution   │              │ - Execution   │
│ - Normalizing │              │ - Normalizing │              │ - Normalizing │
└───────────────┘              └───────────────┘              └───────────────┘
```

---

## 2. Standard `BasePlugin` Interface (Python)

Every plugin MUST subclass an abstract base class with strongly typed contracts:

```python
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List, Dict, Any
from pydantic import BaseModel
import asyncio

TInput = TypeVar("TInput", bound=BaseModel)
TOutput = TypeVar("TOutput", bound=BaseModel)

class PluginMetadata(BaseModel):
    name: str
    version: str
    description: str
    author: str
    tags: List[str]
    rate_limit_per_minute: int = 60
    requires_api_key: bool = False
    supported_target_types: List[str] = ["username", "email", "domain", "ip"]

class BasePlugin(ABC, Generic[TInput, TOutput]):
    metadata: PluginMetadata

    @abstractmethod
    def validate_input(self, target: TInput) -> bool:
        """Validate whether target input is syntactically valid for this plugin."""
        pass

    @abstractmethod
    async def execute(self, target: TInput, config: Dict[str, Any]) -> Any:
        """Execute raw plugin logic (subprocess, API call, scraping)."""
        pass

    @abstractmethod
    def normalize(self, raw_data: Any) -> TOutput:
        """Transform raw plugin output into unified standard domain entity."""
        pass

    async def run_safe(self, target: TInput, config: Dict[str, Any], timeout_seconds: int = 30) -> Optional[TOutput]:
        """Protected runner handling timeouts, errors, and normalization."""
        if not self.validate_input(target):
            raise ValueError(f"Target '{target}' invalid for plugin {self.metadata.name}")
        
        try:
            raw = await asyncio.wait_for(self.execute(target, config), timeout=timeout_seconds)
            return self.normalize(raw)
        except asyncio.TimeoutError:
            raise TimeoutError(f"Plugin {self.metadata.name} timed out after {timeout_seconds}s")
        except Exception as e:
            # Log structured error without crashing orchestrator
            raise RuntimeError(f"Plugin {self.metadata.name} failed: {str(e)}") from e
```

---

## 3. Dynamic Plugin Discovery & Registry

Plugins must be discoverable automatically without hardcoding imports in main apps:

```python
import importlib
import pkgutil
import inspect
from typing import Dict, Type

class PluginRegistry:
    def __init__(self):
        self._plugins: Dict[str, BasePlugin] = {}

    def register(self, plugin: BasePlugin):
        self._plugins[plugin.metadata.name.lower()] = plugin

    def get(self, name: str) -> Optional[BasePlugin]:
        return self._plugins.get(name.lower())

    def list_all(self) -> List[PluginMetadata]:
        return [p.metadata for p in self._plugins.values()]

    def auto_discover(self, package):
        """Scans a Python package and registers all BasePlugin subclasses."""
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            full_module_name = f"{package.__name__}.{module_name}"
            module = importlib.import_module(full_module_name)
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BasePlugin) and obj is not BasePlugin:
                    instance = obj()
                    self.register(instance)
```

---

## 4. Architectural Rules for Plugin Development

1. **Self-Contained Dependencies:** A plugin must not depend on side-effects or global state in other plugins.
2. **Deterministic Output Schemas:** Plugins must never return arbitrary strings or untyped dicts. Every plugin must emit a typed Pydantic output model.
3. **Graceful Degradation:** If a third-party service fails or blocks the plugin, it must raise a structured domain error (`RateLimitError`, `BlockedError`, `NotFoundError`) rather than causing an unhandled exception.
4. **Sandboxed Subprocess Execution:** If calling external CLI binaries (e.g. exiftool, nmap), use `asyncio.create_subprocess_exec` with explicit argument lists (NEVER `shell=True`) and enforce execution timeouts.
