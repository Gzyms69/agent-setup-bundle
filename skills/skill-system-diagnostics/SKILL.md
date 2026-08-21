---
name: skill-system-diagnostics
description: Hardware/OS/driver/kernel diagnostics, log analysis, and root-cause system debugging. MUST ACTIVATE when diagnosing system-level failures, hardware issues, driver incompatibilities, kernel logs (dmesg/journalctl), or memory/CPU bottlenecks.
---

# System Diagnostics & Root Cause Analysis

## Overview

This skill governs all hardware, OS, driver, and kernel-level debugging. It enforces a rigorous diagnostic methodology that prevents speculative fixes and ensures root causes are identified through hard evidence.

## When to Use

- Hardware/OS/driver/kernel debugging
- System performance degradation investigation
- Log analysis (syslog, journalctl, dmesg, application logs)
- Network connectivity or firewall issues
- Disk/filesystem errors or storage failures
- Boot failures, kernel panics, system hangs
- Service failures (systemd units)
- GPU/driver compatibility issues

## When NOT to Use

- Application-level bugs (use `skill-qa-engineer` or `skill-code-review`)
- Cloud infrastructure provisioning (use `skill-devops-cloud`)
- Pure data analysis without system context (use `skill-data-analysis`)

---

## 1. Diagnostic Command Cheatsheet

### System Identity (ALWAYS run first)

```bash
# Hardware baseline
uname -a                        # Kernel version, architecture
cat /proc/cpuinfo | head -20    # CPU model, cores, flags
free -h                         # RAM total/used/available
lsblk -f                        # Block devices, filesystems, mount points
lspci -nn                       # PCI devices (GPU, NIC, controllers)
lsusb                           # USB devices

# GPU & Display
lspci -nn | grep -iE 'vga|3d|display'   # GPU identification
nvidia-smi 2>/dev/null || echo "No NVIDIA driver"  # NVIDIA status
cat /proc/driver/nvidia/version 2>/dev/null         # NVIDIA driver version

# OS & Package Manager
cat /etc/os-release             # Distribution info
dpkg --list | wc -l             # Package count (Debian/Ubuntu)
```

### Log Analysis Commands

```bash
# Kernel & hardware logs
dmesg --level=err,warn -T | tail -50        # Recent kernel errors with timestamps
journalctl -p err -b --no-pager | tail -100 # Errors since last boot
journalctl -u <service> --no-pager -n 50    # Specific service logs

# System events
journalctl --since "1 hour ago" --no-pager  # Recent events
journalctl -k --no-pager | tail -50         # Kernel messages only
last reboot                                 # Reboot history

# Storage diagnostics
smartctl -a /dev/sda 2>/dev/null            # SMART disk health
df -h                                       # Filesystem usage
iostat -x 1 3                               # I/O performance
```

### Network Diagnostics

```bash
ip addr show                    # Interface addresses
ip route show                   # Routing table
ss -tulnp                       # Listening ports with process info
ping -c 3 <host>                # Basic connectivity
traceroute <host>               # Path analysis
nslookup <domain>               # DNS resolution
iptables -L -n 2>/dev/null      # Firewall rules
```

### Process & Performance

```bash
top -bn1 | head -20             # Process snapshot
ps aux --sort=-%mem | head -10  # Top memory consumers
ps aux --sort=-%cpu | head -10  # Top CPU consumers
strace -p <PID> -c              # System call summary
lsof -p <PID>                   # Open files by process
vmstat 1 5                      # Virtual memory statistics
sar -u 1 5                      # CPU utilization history
```

---

## 2. Log Analysis Protocol

Follow this sequence EXACTLY when analyzing logs:

### Step 1: PARSE
- Identify log format (syslog, JSON, plain text, structured)
- Note timestamp format and timezone
- Count total entries and time span covered

### Step 2: CATEGORIZE
- Sort entries by severity: `CRITICAL > ERROR > WARNING > INFO > DEBUG`
- Focus on CRITICAL and ERROR first -- everything else is context

### Step 3: DETECT ANOMALIES
- Look for timestamp clusters (multiple errors within seconds = cascade)
- Identify irregular spikes in frequency
- Cross-correlate timestamps across different log sources (kernel + application + service)
- Check for patterns: repeated errors, periodic failures, growing intervals

### Step 4: IDENTIFY ROOT CAUSE
- Trace the FIRST error in a cascade -- that is the likely root cause
- Map out the fault domain: which component(s) are affected?
- Differentiate SYMPTOMS (secondary failures) from CAUSE (initial trigger)
- Check if the error matches known patterns (search_web for error codes)

### Step 5: FORMULATE REMEDIATION
- Create minimal reproduction steps
- Identify environmental triggers (specific kernel version, driver version, load condition)
- Propose fix that addresses ROOT CAUSE, not symptoms

---

## 3. Root Cause Analysis Process

### Fault Domain Mapping

```
[Trigger Event] --> [Primary Failure] --> [Cascade Effect 1] --> [Cascade Effect N]
                                      \-> [Cascade Effect 2]
```

1. **Ingest** all available evidence (stack traces, logs, error codes, user observations)
2. **Map** the fault domain: identify which system boundaries are affected
3. **Differentiate** between secondary symptomatic errors and the initial root cause trigger
4. **Timeline** the events: what happened FIRST? That is your investigation starting point
5. **Reproduce** minimally: strip away variables until you have the smallest trigger
6. **Verify** the fix resolves the ORIGINAL symptom, not just silences the error

### Symptom vs Cause Decision Tree

| Observation | Likely Category |
|-------------|----------------|
| Error appears FIRST in timeline | Potential ROOT CAUSE |
| Error appears AFTER another error | SYMPTOM (investigate upstream) |
| Error disappears when upstream is fixed | Confirmed SYMPTOM |
| Error persists after upstream fix | Independent ROOT CAUSE |
| Error is intermittent | Environmental trigger (load, race condition, resource exhaustion) |

---

## 4. Output Format

When reporting diagnostics, use this structure:

### LOG SUMMARY
- Time range analyzed
- Total events by severity
- Overall system health assessment: `HEALTHY / DEGRADED / CRITICAL`

### ANOMALIES & ERROR PATTERNS
- Clustered error events with timestamps
- Frequency analysis
- Cross-component correlations

### ROOT CAUSE ANALYSIS
- Primary defect identified
- Evidence chain (specific log lines, error codes)
- Symptom vs cause mapping

### REMEDIATION PLAN
- Immediate fix (specific commands/changes)
- Verification steps (how to confirm the fix works)
- Long-term prevention (monitoring, configuration changes)

---

## 5. Anti-Rationalization Table

| Agent Rationalization | BLOCKED Response |
|:---|:---|
| *"I know what this error means from experience."* | BLOCKED: Verify with `search_web` or official docs. Internal knowledge may be outdated or wrong. |
| *"The logs look clean, so the issue is elsewhere."* | BLOCKED: Absence of errors in one log source does not mean no errors exist. Check ALL log sources (dmesg, journalctl, application logs, syslog). |
| *"I'll just restart the service to fix it."* | BLOCKED: Restarting masks the root cause. Diagnose WHY the service failed before restarting. |
| *"This is probably a driver issue, let me reinstall."* | BLOCKED: Reinstalling is forbidden as a first step. Run `dmesg`, check driver version, verify compatibility FIRST. |
| *"The user says it was working before, so it's a recent change."* | BLOCKED: Correlation is not causation. Verify with `journalctl --since`, package update history (`apt history`), and config diff. |
| *"I can't reproduce it, so it might be a fluke."* | BLOCKED: Intermittent issues have environmental triggers. Check load patterns, resource exhaustion, race conditions, thermal throttling. |
| *"Let me change this config value, it should help."* | BLOCKED: Every config change MUST reference a specific log line or error code that justifies it. No speculative tuning. |

---

## 6. Red Flags

- Proposing a fix without citing specific log lines or error codes
- Skipping `dmesg` or `journalctl` when debugging system issues
- Assuming hardware specs instead of running diagnostic commands
- Changing kernel parameters or system config without root cause evidence
- Declaring "fixed" without re-running the originally failing operation
- Investigating application code when the error is clearly in system logs
- Using `sudo` commands without explaining WHY root access is needed

---

## 7. Verification Gates

1. **Evidence Gate**: Every diagnosis MUST cite at least one specific log line, error code, or command output
2. **Reproduction Gate**: Root cause hypothesis MUST include reproduction steps (or explain why reproduction is not possible)
3. **Fix Verification Gate**: After applying a fix, the ORIGINAL failing operation MUST be re-run to confirm resolution
4. **No Regression Gate**: Verify that the fix does not introduce new errors in related components (check logs post-fix)
5. **Documentation Gate**: Record the diagnosis, root cause, and fix in a format the user can reference later
