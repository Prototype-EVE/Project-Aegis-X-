import psutil
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def monitor_system():
    print("🛡️  AEGIS-X: SYSTEM HEALTH DASHBOARD (M2 NATIVE)")
    print("=" * 50)
    
    try:
        while True:
            # 1. CPU & RAM LOAD
            cpu_usage = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory()
            
            # 2. DISK IO (Tracking the Black Box activity)
            disk = psutil.disk_io_counters()
            
            clear_screen()
            print("🛡️  AEGIS-X: SYSTEM HEALTH DASHBOARD")
            print("=" * 50)
            print(f"CORE LOAD:   [{'|' * int(cpu_usage/2)}{'-' * (50-int(cpu_usage/2))}] {cpu_usage}%")
            print(f"MEMORY:      {ram.percent}% Used ({ram.available / 1024 / 1024:.0f}MB Available)")
            print(f"BLACK BOX:   {disk.write_bytes / 1024 / 1024:.2f} MB Written to disk")
            print("-" * 50)
            
            # 3. CRITICAL THRESHOLD ALERT
            if cpu_usage > 90:
                print("⚠️  WARNING: High CPU Load. Signal processing may be delayed.")
            if ram.percent > 90:
                print("⚠️  WARNING: Memory Pressure detected. Check for 'Ghost' processes.")
                
            print("\n[Press CTRL+C to Exit]")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nHealth Monitoring Suspended.")

if __name__ == "__main__":
    monitor_system()
