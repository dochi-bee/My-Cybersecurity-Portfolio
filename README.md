# SSH Brute-Force Log Analyzer

A lightweight Python security tool that parses Linux SSH authentication logs (`auth.log`) to detect and flag potential brute-force login attempts.

## Project Overview
In corporate Security Operations Centers (SOCs), analysts monitor authentication logs to identify unauthorized access attempts. This script automates the triage process by scanning server logs, extracting source IP addresses from failed login events, and alerting when an IP crosses a defined failure threshold.

## Tools & Technologies
* **Language:** Python 3
* **Modules:** `re` (Regular Expressions), `collections` (`defaultdict`)
* **Environment:** Windows 11 / Linux SSH Logs

## How It Works
1. **Log Ingestion:** Reads raw authentication logs line by line.
2. **Pattern Matching:** Filters for `"Failed password"` entries and extracts IPv4 addresses using regex.
3. **Threshold Alerting:** Counts failed attempts per IP and triggers a `[ALERT]` warning if an IP exceeds 3 failed logins.

## How to Run
1. Clone this repository or download `log_analyzer.py` and `auth.log` into the same folder.
2. Run the script in your terminal:
   ```bash
   python log_analyzer.py
   ```
<img width="1920" height="1080" alt="Screenshot (253)" src="https://github.com/user-attachments/assets/2e188452-df77-4cbf-86e1-371af74612d3" />


