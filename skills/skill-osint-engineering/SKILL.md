---
name: skill-osint-engineering
description: Open Source Intelligence (OSINT) engineering principles, standardized entity graph models, pivoting engines, reconnaissance pipelines, and OPSEC best practices. Use when designing OSINT platforms, writing intelligence scrapers, mapping entity relationships, or implementing forensic analyzers.
---

# OSINT Engineering Skill

This skill defines the technical standards, entity relationship models, and operational security (OPSEC) frameworks for developing Open Source Intelligence (OSINT) automation platforms and investigative tools.

---

## 1. Unified Entity Data Model (Pydantic Standard)

All OSINT tools, plugins, and scrapers MUST produce entities conforming to a unified entity graph schema:

```python
from enum import Enum
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class EntityType(str, Enum):
    PERSON = "person"
    USERNAME = "username"
    EMAIL = "email"
    PHONE = "phone"
    DOMAIN = "domain"
    IP_ADDRESS = "ip_address"
    SOCIAL_PROFILE = "social_profile"
    BREACH_RECORD = "breach_record"
    METADATA_EXTRACT = "metadata_extract"
    CRYPTO_WALLET = "crypto_wallet"

class OSINTEntity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    entity_type: EntityType
    value: str  # e.g., "jankowalski@example.com" or "192.168.1.1"
    source_tool: str  # e.g., "holehe", "sherlock", "theHarvester"
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    discovered_at: datetime = Field(default_factory=datetime.utcnow)
    attributes: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)

class OSINTRelationship(BaseModel):
    source_entity_id: str
    target_entity_id: str
    relation_type: str  # e.g., "HAS_EMAIL", "USES_USERNAME", "REGISTERED_ON"
    source_tool: str
    confidence: float = 1.0

class OSINTInvestigationGraph(BaseModel):
    target: str
    entities: List[OSINTEntity] = []
    relationships: List[OSINTRelationship] = []

    def add_entity(self, entity: OSINTEntity):
        self.entities.append(entity)

    def add_link(self, source_id: str, target_id: str, relation_type: str, tool: str):
        self.relationships.append(OSINTRelationship(
            source_entity_id=source_id,
            target_entity_id=target_id,
            relation_type=relation_type,
            source_tool=tool
        ))
```

---

## 2. The OSINT Reconnaissance Lifecycle

Automated OSINT systems must strictly adhere to the phased recon workflow:

```
[Phase 1: Input Validation & Sanitization]
      │
      ▼
[Phase 2: Passive Footprinting (DNS, WHOIS, Public APIs, Caches)]
      │
      ▼
[Phase 3: Active Scans (Social Profiles, Port Probes, Breach Lookups)]
      │
      ▼
[Phase 4: Normalization & Deduplication]
      │
      ▼
[Phase 5: Entity Graph Correlation & Pivot Suggestions]
```

### Pivoting Engine
When an investigation runs, any discovered sub-entity (e.g. finding an email address during a username scan) can be queued as a **Pivot Target** for subsequent plugin executions:
- `Username -> Social Profile -> Email Address (Pivot 1)`
- `Email Address -> Breach Database -> Leaked Password Hash / Linked Accounts (Pivot 2)`
- `Domain -> WHOIS registrant -> Associated Domains (Pivot 3)`

---

## 3. Operational Security (OPSEC) & Privacy Mandates

1. **Passive Recon by Default:** Never send active probing packets (e.g. port scans, direct form submissions) without explicit user consent.
2. **Rotating Identity & User-Agents:** Always randomize realistic User-Agents matching modern Chromium browsers.
3. **Proxy & Tor Routing:** Route high-frequency scrapers through proxy pools (SOCKS5 / HTTP proxies / Tor) to prevent analyst IP address exposure.
4. **API Key Security:** Store API keys in environment variables or encrypted credential vaults. Never commit secrets to code or log unredacted headers.
5. **Rate-Limiting & Jitter:** Add randomized delays (jitter) between requests (e.g., `1.5s - 3.5s`) to prevent IP bans and respect target robots.txt/terms.
