import re
from collections import defaultdict

# Configuration
LOG_FILE = "auth.log"
THRESHOLD = 3

def analyze_logs(file_path, threshold):
    failed_attempts = defaultdict(int)
    
    # Regular expression to extract IPv4 addresses
    ip_pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")

    try:
        with open(file_path, "r") as file:
            for line in file:
                if "Failed password" in line:
                    match = ip_pattern.search(line)
                    if match:
                        ip_address = match.group()
                        failed_attempts[ip_address] += 1
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return

    print("=== SECURITY LOG ANALYSIS REPORT ===")
    print(f"Alert Threshold: {threshold}+ failed login attempts\n")

    flagged = False
    for ip, count in failed_attempts.items():
        if count >= threshold:
            print(f"[ALERT] Potential Brute-Force Attack from {ip} ({count} failed attempts)")
            flagged = True
        else:
            print(f"[INFO] Normal activity / minor failure from {ip} ({count} failed attempt)")

    if not flagged:
        print("No brute-force activity detected.")

if __name__ == "__main__":
    analyze_logs(LOG_FILE, THRESHOLD)
