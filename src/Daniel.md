{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11540\viewh8420\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #!/bin/bash\
\
# Aegis-X Master Controller - Commander Edition (UK English)\
# Purpose: Launches Tri-Node Defense Stack with Auditory Feedback\
\
# Voice Settings - Targeting "Oliver" (UK Male)\
VOICE="Oliver" \
\
announce() \{\
  # This command specifically requests the UK Male voice\
  say -v "$VOICE" "$1" || say "$1"\
  echo "\uc0\u55357 \u56546  [SYSTEM VOICE]: $1"\
\}\
\
# --- STARTUP SEQUENCE ---\
announce "Initializing Aegis-X Cockpit. Scanning local spectrum for anomalies."\
\
open_tab() \{\
  osascript <<EOF\
    tell application "Terminal"\
      activate\
      do script "cd $(pwd) && source ~/miniforge3/bin/activate && $1"\
    end tell\
EOF\
\}\
\
# 1. System Health\
open_tab "python aegis_health.py"\
announce "Hardware vitals node is online. M2 silicon is nominal."\
\
# 2. Frequency Sensor\
open_tab "python aegis_sensor_pro.py"\
announce "Frequency sensor engaged. The Black Box is now recording forensic data."\
\
# 3. AI Bridge\
open_tab "interpreter --local --model ollama/llama3.1"\
announce "Llama 3.1 intelligence bridge established. Sovereign defense is active."\
\
announce "System check complete. You have the bridge, Alt."}