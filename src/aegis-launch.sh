#!/bin/bash

# --- AEGIS-X STEALTH LAUNCHER ---
# This script opens three tiled windows in 'Homebrew' (Green/Black) mode.

# 1. Launch the Sensor (The Watchman)
osascript -e 'tell application "Terminal" to do script "cd \"/Users/joelgarcia/Desktop/Project Aegis-X/src\" && python3 aegis_sensor_pro.py"' \
          -e 'tell application "Terminal" to set current settings of window 1 to settings set "Homebrew"'

# 2. Launch the Auditor (The Record Keeper)
osascript -e 'tell application "Terminal" to do script "cd \"/Users/joelgarcia/Desktop/Project Aegis-X/src\" && python3 aegis_auditor.py"' \
          -e 'tell application "Terminal" to set current settings of window 1 to settings set "Homebrew"'

# 3. Launch the Health Monitor (The Vital Sign)
osascript -e 'tell application "Terminal" to do script "cd \"/Users/joelgarcia/Desktop/Project Aegis-X/src\" && python3 aegis_health.py"' \
          -e 'tell application "Terminal" to set current settings of window 1 to settings set "Homebrew"'

echo "🟢 STEALTH MODE ENGAGED. COCKPIT TILING IN GREEN-ON-BLACK."
say -v Daniel "Stealth mode engaged. The matrix is active."
