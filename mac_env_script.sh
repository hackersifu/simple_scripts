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