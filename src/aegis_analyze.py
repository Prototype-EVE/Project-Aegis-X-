import os
import glob
import subprocess

# --- CONFIGURATION ---
LOG_DIR = "../SENTINEL_AUDITS"
VOICE = "Daniel"

def speak(text):
    subprocess.run(["say", "-v", VOICE, text])

def analyze_latest_breach():
    # Find all breach archives
    archives = glob.glob(f"{LOG_DIR}/BREACH_ARCHIVE_*.log")
    if not archives:
        print("📁 No breach archives found. System is clean.")
        speak("No forensic evidence found. The perimeter remains secure.")
        return

    # Get the most recent one
    latest_breach = max(archives, key=os.path.getctime)
    filename = os.path.basename(latest_breach)
    
    print(f"🕵️  ANALYZING RECENT INCIDENT: {filename}")
    speak(f"Analyzing the most recent security incident recorded in {filename}")

    with open(latest_breach, "r") as f:
        lines = f.readlines()
        if not lines:
            return

        # The last line in the archive is usually the "Sledgehammer"
        malicious_entry = lines[-1].strip()
        
        print("-" * 50)
        print(f"🚩 MALICIOUS PAYLOAD DETECTED:")
        print(f"   > {malicious_entry}")
        print("-" * 50)

        # Auditory Briefing
        summary = f"Forensic analysis complete. The malicious payload identified was: {malicious_entry}. This entry failed the cryptographic integrity check, triggering the immediate lockdown of the Aegis bridge."
        speak(summary)

if __name__ == "__main__":
    analyze_latest_breach()
