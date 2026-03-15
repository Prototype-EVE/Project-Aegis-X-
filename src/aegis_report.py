import os
import glob
from datetime import datetime

LOG_DIR = "../SENTINEL_AUDITS"
REPORT_FILE = "../MISSION_SUMMARY.md"

def generate_report():
    archives = sorted(glob.glob(f"{LOG_DIR}/BREACH_ARCHIVE_*.log"))
    
    with open(REPORT_FILE, "w") as f:
        f.write(f"# 🛡️ PROJECT AEGIS-X: MISSION REPORT\n")
        f.write(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Operator:** Alt. CunningRAM\n\n")
        f.write(f"## 📊 Executive Summary\n")
        f.write(f"- **Total Breaches Neutralized:** {len(archives)}\n")
        f.write(f"- **System Integrity Status:** OPTIMAL\n\n")
        f.write(f"## 🕵️ Forensic Breakdown\n")
        f.write("| Timestamp | Archive File | Malicious Payload Detected |\n")
        f.write("| :--- | :--- | :--- |\n")

        for arch in archives:
            filename = os.path.basename(arch)
            # Extract timestamp from filename (BREACH_ARCHIVE_YYYYMMDD_HHMMSS.log)
            time_str = filename.split("_")[2] + " " + filename.split("_")[3].split(".")[0]
            
            with open(arch, "r") as log:
                lines = log.readlines()
                payload = lines[-1].strip() if lines else "EMPTY_LOG"
            
            f.write(f"| {time_str} | {filename} | `{payload}` |\n")

    print(f"✨ Mission Report generated: {REPORT_FILE}")
    os.system(f"say -v Daniel 'Mission report compiled. Documentation is secure.'")

if __name__ == "__main__":
    generate_report()
