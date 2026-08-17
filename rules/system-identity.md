# System Identity Baseline Template

This file establishes a machine-readable hardware and OS baseline for the AI coding agent to prevent hardware hallucination and ensure accurate compiler/tooling flags.

## Hardware Baseline (Example / Template)
- CPU: Fill with `lscpu` or `cat /proc/cpuinfo` (e.g. x86_64 / ARM64, Cores/Threads)
- GPU: Fill with `lspci | grep -i vga` or `nvidia-smi`
- RAM: Fill with `free -h` (e.g. 16GB, 32GB, 64GB)
- System Disk: Primary NVMe/SSD mount point

## OS & Kernel
- OS: Fill with `cat /etc/os-release` (e.g. Ubuntu 24.04 LTS / Debian / Fedora / macOS)
- Kernel: `uname -r`
- Display Server: Wayland / X11

## Workspace Layout
- `~/Dev Projects/` -- Primary development workspace
- `~/.agents/` -- Unified agent rules & skills (`rules/`, `skills/`)
- `~/.gemini/` -- Antigravity & Gemini CLI configuration
- `~/.claude/` -- Claude Code configuration & subagents
- `~/.cursor/` -- Cursor IDE rules and MCP configuration

## Important
- Hardware, drivers, and package versions change over time.
- Always run live diagnostic commands (`uname -a`, `free -h`, `lspci`) before making architectural assumptions.
