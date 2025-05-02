#!/bin/bash

# Open Mission Control and simulate a keystroke to add a new desktop
osascript <<EOF
tell application "System Events"
    key down control
    key code 126 -- Up arrow for Mission Control
    delay 0.5
    key code 124 -- Right arrow to go to the end
    delay 0.5
    key code 44 using {control down} -- Press Control + Right to move to new space
    key up control
end tell
EOF