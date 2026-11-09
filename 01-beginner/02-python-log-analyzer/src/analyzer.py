
from collections import Counter
from pathlib import Path
import re

# Locate the log file relative to this script.
LOG_FILE = Path(__file__).resolve().parent.parent / "logs" / "auth.log"

# Minimum number of failed attempts required to trigger an alert.
ALERT_THRESHOLD = 3

# Match failed SSH password events and capture their source IP.
FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password .* from (\d{1,3}(?:\.\d{1,3}){3}) port "
)


def analyze_logs(file_path):
    failed_attempts = Counter()

    with open(file_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            match = FAILED_LOGIN_PATTERN.search(line)

            if match:
                ip_address = match.group(1)
                failed_attempts[ip_address] += 1

    return failed_attempts


def main():
    try:
        results = analyze_logs(LOG_FILE)
    except FileNotFoundError:
        print(f"Error: Log file not found: {LOG_FILE}")
        return

    print("=== Python Log Analyzer ===")
    print(f"Total failed login attempts: {sum(results.values())}")
    print()

    print("Failed attempts by IP:")
    for ip_address, count in results.most_common():
        print(f"  {ip_address}: {count}")

    print()
    print(f"Potentially suspicious IPs (threshold: {ALERT_THRESHOLD}):")

    suspicious_ips = {
        ip_address: count
        for ip_address, count in results.items()
        if count >= ALERT_THRESHOLD
    }

    if suspicious_ips:
        for ip_address, count in sorted(
            suspicious_ips.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(f"  [ALERT] {ip_address}: {count} failed attempts")
    else:
        print("  No IPs exceeded the alert threshold.")


if __name__ == "__main__":
    main()
