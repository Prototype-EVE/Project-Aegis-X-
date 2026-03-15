import hashlib
import os
import subprocess

# --- CONFIGURATION ---
LOG_PATH = "../SENTINEL_AUDITS/Aegis_BlackBox.log"
VOICE = "Daniel"

def speak(text):
    subprocess.run(["say", "-v", VOICE, text])

def verify_integrity():
    if not os.path.exists(LOG_PATH):
        speak("Error. Forensic log not found.")
        return

    speak("Commencing internal audit of the Aegis Black Box.")
    
    valid_count = 0
    tampered_count = 0

    if os.path.getsize(LOG_PATH) == 0:
        speak("The log is currently empty. No entries to verify.")
        return

    with open(LOG_PATH, "r") as f:
        for line in f:
            if not line.strip(): continue
            try:
                parts = line.split(" | ")
                timestamp = parts[0].strip("[] ")
                data_part = parts[1].replace("DATA: ", "")
                stored_sig = parts[2].replace("SIGNATURE: ", "").strip()

                raw_string = f"{timestamp}{data_part}"
                expected_sig = hashlib.sha256(raw_string.encode()).hexdigest()

                if expected_sig == stored_sig:
                    valid_count += 1
                else:
                    tampered_count += 1
            except:
                tampered_count += 1

    if tampered_count == 0:
        msg = f"Audit complete. {valid_count} entries verified. Log integrity is secure."
        print(f"✅ {msg}")
        speak(msg)
    else:
        msg = f"Critical alert. {tampered_count} entries have been altered."
        print(f"🚨 {msg}")
        speak(msg)

if __name__ == "__main__":
    verify_integrity()
