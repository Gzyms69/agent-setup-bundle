# Command Outcome Verification

Never assume a command succeeded based solely on exit code.

For any command with side effects:
1. DEFINE expected outcome BEFORE execution.
2. EXECUTE the command.
3. VERIFY outcome with a secondary, read-only check.

Examples:
- After mkdir: ls to confirm directory exists.
- After npm install: check package.json or node_modules.
- After git commit: git log -1 to confirm.
- After file write: view_file to confirm content.
- After service restart: systemctl status to confirm running.
- After package removal: dpkg -l or apt list to confirm gone.
- After config change: cat the config file to confirm edit took effect.
