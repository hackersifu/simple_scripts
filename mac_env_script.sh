#!/bin/bash

osascript <<EOF
tell application "System Events"
    set appList to name of every process whose background only is false and name is not "Finder"
    repeat with appName in appList
        try
            tell application appName to quit
        end try
    end repeat
end tell
EOF

osascript <<'END'
tell application "System Events"
    set appsToClose to (name of every application process where background only is false) ¬
        whose name is not "Finder" and name is not "Terminal"
    repeat with appName in appsToClose
        try
            tell application appName to quit
        end try
    end repeat
end tell
END

# Optional: wait for a moment to let apps close cleanly
sleep 3