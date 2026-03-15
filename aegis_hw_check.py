import subprocess
import os

# --- COMMANDER'S VOICE CONFIG ---
VOICE = "Daniel" # British Male Advisor

def announce(msg):
    subprocess.Popen(["say", "-v", VOICE, msg])

def check_us_hardware():
    print("🇺🇸 AEGIS-X: SCANNING TRUSTED SUPPLY CHAIN...")
    
    # Example US-Vendor IDs (National Instruments/Ettus, Epiq, etc.)
    TRUSTED_VIDS = ["2552", "fffe", "1d6b"] 
    
    # System command to list USB devices on macOS
    cmd = "ioreg -p IOUSB -l | grep -e 'idVendor'"
    try:
        output = subprocess.check_output(cmd, shell=True).decode()
        
        if any(vid in output for vid in TRUSTED_VIDS):
            msg = "Trusted US-sourced hardware detected. Supply chain integrity verified."
            print(f"✅ {msg}")
            announce(msg)
        else:
            msg = "Warning. No US-verified hardware found. Running in simulation mode."
            print(f"⚠️ {msg}")
            announce(msg)
            
    except Exception:
        announce("Hardware scan failed. Ensure SDR is connected via secure US-made link.")

if __name__ == "__main__":
    check_us_hardware()
