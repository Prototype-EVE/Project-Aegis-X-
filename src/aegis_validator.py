import hashlib
import os

# --- CONFIGURATION ---
LOG_PATH = "SENTINEL_AUDITS/Aegis_BlackBox.log"

def verify_logs():
    if not os.path.exists(LOG_PATH):
        print(f"❌ ERROR: Log file not found at {LOG_PATH}. Start the sensor first.")
        return

    print("🛡️  AEGIS-X: COMMENCING FORENSIC INTEGRITY AUDIT...")
    print("-" * 60)

    valid_count = 0
    tampered_count = 0
    total_entries = 0

    with open(LOG_PATH, "r") as f:
        for line_num, line in enumerate(f, 1):
            if not line.strip(): continue
            total_entries += 1
            
            try:
                # 1. PARSE THE LOG ENTRY
                # Format: [timestamp] | DATA: data_str | SIGNATURE: signature
                parts = line.split(" | ")
                timestamp = parts[0].strip("[] ")
                data_part = parts[1].replace("DATA: ", "")
                stored_signature = parts[2].replace("SIGNATURE: ", "").strip()

                # 2. RE-CALCULATE THE HASH
                # Logic must match aegis_sensor_pro.py
                raw_string = f"{timestamp}{data_part}"
                expected_signature = hashlib.sha256(raw_string.encode()).hexdigest()

                # 3. VERIFY INTEGRITY
                if expected_signature == stored_signature:
                    valid_count += 1
                else:
                    print(f"🚨 TAMPER ALERT: Entry {line_num} has a mismatched signature!")
                    print(f"   Stored: {stored_signature[:10]}...")
                    print(f"   Calculated: {expected_signature[:10]}...")
                    tampered_count += 1

            except Exception as e:
                print(f"⚠️  CORRUPTION ALERT: Failed to parse Line {line_num}. Possible manual deletion attempt.")
                tampered_count += 1

    # --- FINAL REPORT ---
    print("-" * 60)
    print(f"AUDIT COMPLETE.")
    print(f"✅ Verified Entries: {valid_count}")
    print(f"🚫 Tampered/Corrupt: {tampered_count}")
    
    if tampered_count == 0:
        print("\n🏆 RESULT: LOG INTEGRITY 100% SECURE. NO TAMPERING DETECTED.")
    else:
        print("\n🛑 RESULT: CRITICAL FAILURE. LOG FILE HAS BEEN ALTERED.")

if __name__ == "__main__":
    verify_logs()
