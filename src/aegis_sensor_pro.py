import hashlib
import time
import os
import subprocess
import sys

# --- CONFIGURATION ---
LOG_PATH = "../SENTINEL_AUDITS/Aegis_BlackBox.log"
VOICE = "Daniel"
CHECK_INTERVAL = 1  # Audit every single entry for the stress test

def speak(text):
    # 'say' can sometimes hang if not handled right; we'll use a timeout
    try:
        subprocess.run(["say", "-v", VOICE, text], timeout=5)
    except:
        print(f"🔊 [VOICE ERROR]: {text}")

def verify_integrity():
    if not os.path.exists(LOG_PATH) or os.path.getsize(LOG_PATH) == 0:
        return True
    
    try:
        with open(LOG_PATH, "r") as f:
            for line in f:
                line = line.strip()
                if not line: continue
                
                # FORTIFIED PARSING: Check if the line has the expected format
                if " | DATA: " not in line or " | SIGNATURE: " not in line:
                    return False # Malformed line is a breach!
                
                parts = line.split(" | ")
                timestamp = parts[0].strip("[] ")
                data_part = parts[1].replace("DATA: ", "")
                stored_sig = parts[2].replace("SIGNATURE: ", "").strip()
                
                raw_string = f"{timestamp}{data_part}"
                expected_sig = hashlib.sha256(raw_string.encode()).hexdigest()
                
                if expected_sig != stored_sig:
                    return False
    except Exception as e:
        print(f"⚠️ Audit internal error: {e}")
        return False
    return True

def run_sensor():
    count = 0
    print("🛡️  AEGIS-X: High-Sensitivity Mode Active.")
    speak("Sovereign Sensor Online. High sensitivity enabled.")
    
    try:
        while True:
            # INTEGRITY CHECK (Every cycle)
            if not verify_integrity():
                msg = "CRITICAL BREACH DETECTED. LOG INTEGRITY COMPROMISED. AUTO LOCKING SYSTEM."
                print(f"\n🚨 {msg}")
                speak(msg)
                sys.exit(1)

            # LOGGING LOGIC
            ts = time.strftime("%Y-%m-%d %H:%M:%S")
            data = f"FREQ_SCAN_{count:03d}"
            sig = hashlib.sha256(f"{ts}{data}".encode()).hexdigest()
            log_entry = f"[{ts}] | DATA: {data} | SIGNATURE: {sig}\n"
            
            with open(LOG_PATH, "a") as f:
                f.write(log_entry)
            
            print(f"🛰️  Scan {count:03d} | [SECURE]", end="\r")
            count += 1
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping...")
        speak("Sensor standing down.")

if __name__ == "__main__":
    run_sensor()
