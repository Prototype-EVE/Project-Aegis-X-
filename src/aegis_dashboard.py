import os
import glob
import subprocess

# --- CONFIGURATION ---
LOG_DIR = "../SENTINEL_AUDITS"
CURRENT_LOG = f"{LOG_DIR}/Aegis_BlackBox.log"
VOICE = "Daniel"

def speak(text):
    subprocess.run(["say", "-v", VOICE, text])

def get_stats():
    # Count verified scans in the current log
    scans = 0
    if os.path.exists(CURRENT_LOG):
        try:
            with open(CURRENT_LOG, "r") as f:
                scans = sum(1 for line in f if "SIGNATURE:" in line)
        except:
            scans = 0

    # Count archived breach files (the "Wall of Trophies")
    breach_files = glob.glob(f"{LOG_DIR}/BREACH_ARCHIVE_*.log")
    total_breaches = len(breach_files)

    # Visual Output
    print("\n" + "🛡️ " * 10)
    print("      PROJECT AEGIS-X: SHIELD STATUS")
    print("      OPERATOR: ALT. CUNNINGRAM")
    print("-" * 40)
    print(f"✅ VERIFIED SCANS IN LOG: {scans}")
    print(f"🚨 NEUTRALIZED BREACHES: {total_breaches}")
    print("-" * 40)

    # Auditory Briefing
    status_msg = f"Dashboard active. You have {scans} verified entries and you have neutralized {total_breaches} unauthorized breaches today. System status is optimal."
    speak(status_msg)

if __name__ == "__main__":
    get_stats()
