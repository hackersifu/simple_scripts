#!/bin/bash

echo "Force-closing all user applications..."

# Get all visible GUI apps (excluding Finder and Terminal)
apps_to_kill=$(osascript <<'EOF'
tell application "System Events"
    set appList to name of every application process where background only is false
end tell
return appList
EOF
)

# Loop through each app and kill it (except Terminal and Finder)
while IFS= read -r app; do
    if [[ "$app" != "Finder" && "$app" != "Terminal" ]]; then
        echo "Killing $app"
        killall "$app" 2>/dev/null
    fi
done <<< "$apps_to_kill"

sleep 2