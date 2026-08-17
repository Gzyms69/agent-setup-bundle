# Environment Integrity Protocol

For environment-specific errors (e.g., "works on server but not locally",
"works in one terminal but not another", "broke after reboot"):

1. Perform FULL environment audit BEFORE modifying any source code:
   - Check running processes: ps aux, systemctl status, pgrep
   - Check cache state: npm cache, build cache, browser cache
   - Check permissions: ls -la, stat, getfacl
   - Check env variables: env, printenv, echo $VARIABLE
   - Check port conflicts: ss -tuln, lsof -i
   - Check disk space: df -h, du -sh
   - Check kernel logs: dmesg --level=err, journalctl -b -p err
   - Check GPU state: cat /sys/class/drm/card*/device/power_state

2. ONLY after audit eliminates environment causes: modify application code.
3. Document the audit findings before proposing changes.
4. If environment is the cause: fix the environment, not the code.
