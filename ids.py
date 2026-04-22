import re
import time
from collections import defaultdict

LOG_FILE = "/var/log/auth.log"
THRESHOLD = 3

failed_attempts = defaultdict(int)
blocked_ips = set()

def extract_ip(line):
    match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
    return match.group(1) if match else None

def monitor_logs():
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # move to end of file

        while True:
            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            if "Failed password" in line:
                ip = extract_ip(line)
                if ip:
                    failed_attempts[ip] += 1
                    print(f"[INFO] Failed attempt from {ip} ({failed_attempts[ip]})")

                    if failed_attempts[ip] >= THRESHOLD and ip not in blocked_ips:
                        alert_and_block(ip)

def alert_and_block(ip):
    print(f"\n[ALERT] Brute-force attack detected from {ip}")
    print(f"[ACTION] Blocking IP: {ip}\n")

    blocked_ips.add(ip)

    # Real system:
    # os.system(f"sudo ufw deny from {ip}")

if __name__ == "__main__":
    monitor_logs()
