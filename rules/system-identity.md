# System Identity -- gzyms workstation

## Hardware
- Motherboard: Gigabyte Z790 AORUS ELITE AX (BIOS FL, 2025-06-19)
- CPU: Intel Core i5-14600KF (14C/20T, Raptor Lake Refresh, up to 5.30 GHz)
- GPU: AMD Radeon RX 9060 XT (RDNA 4, Navi 44, 16GB VRAM, amdgpu/Mesa)
- RAM: 32 GB DDR5
- System disk: Goodram PX600 1TB NVMe PCIe Gen4 x4 (/dev/nvme0n1)

## OS
- Ubuntu 24.04.4 LTS (Noble Numbat)
- Kernel: Linux 6.17.x (x86_64) -- verify current version with `uname -r`
- Display server: Wayland (GNOME)
- GPU driver: amdgpu (Mesa radeonsi, gfx1200)

## External storage
- Polion USSD 512GB (USB SSD)
- Toshiba MQ01ABD100 1TB HDD (Ugreen enclosure)
- SanDisk 3.2 Gen1 256GB (pendrive)
- KIOXIA TransMemory 256GB (pendrive)

## Disk partitions (baseline -- verify with lsblk)
- /dev/nvme0n1p1: EFI System Partition (~1GB)
- /dev/nvme0n1p2: Linux filesystem (~930GB, ext4, /)

## Workspace layout
- ~/Dev Projects/ -- all development projects
- ~/.agents/ -- AGY CLI workspace config (skills/, rules/)
- ~/.gemini/ -- shared Gemini/AGY config directory (GEMINI.md lives here)
- ~/.gemini/antigravity-cli/ -- AGY CLI app data (settings, brain, MCP config)
- ~/.gemini/config/ -- global config (plugins/, MCP servers)

## IMPORTANT
- Driver versions, kernel versions, and package versions CHANGE.
  Always verify current versions with live diagnostic commands.
- This file provides BASELINE identity to prevent hallucination,
  NOT a substitute for live diagnostic commands.
- When in doubt: run the command, don't guess from this file.
