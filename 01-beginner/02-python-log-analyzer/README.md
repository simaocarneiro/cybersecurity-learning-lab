**Python Log Analyzer**

*Overview*

A Python-based security log analysis tool designed to identify failed SSH authentication attempts, aggregate events by source IP address, and flag repeated failures.

This project uses synthetic authentication logs to demonstrate basic log parsing and threshold-based security monitoring.

**Objectives**

- Parse SSH authentication log entries.
- Identify failed password authentication events.
- Count failed attempts by source IP address.
- Flag IP addresses that reach a configurable alert threshold.
- Validate core functionality using automated unit tests.

**Technologies**

- Python 3
- Python standard library (re, collections, pathlib)
- unittest
- Ubunut Linux
- Git

**Project Structure**

02-python-log-analyzer/
├── README.md
├── docs/
├── logs/
│   └── auth.log
├── src/
│   └── analyzer.py
└── tests/
    └── test_analyzer.py

**Usage**

From the repository root, run:

python3 01-beginner/02-python-log-analyzer/src/analyzer.py

**Example Output**

=== Python Log Analyzer ===
Total failed login attempts: 5

Failed attempts by IP:
  192.0.2.30: 3
  192.0.2.10: 2

Potentially suspicious IPs (threshold: 3):
  [ALERT] 192.0.2.30: 3 failed attempts

**Automated Testing**

Run the unit tests from the repository root:

python3 -m unittest discover -s 01-beginner/02-python-log-anakyzer/tests -p "test_*.py" -v

Three unit test passed during development.

**Security Considerations**

- All included authentication logs are synthetic.
- IP addresses belong to documentation-only address ranges.
- The alert threshold is a demonstration rule, not proof of malicious activity.
- The current parser targets a specific SSH failed-password log format.
- Events are aggregated across the etire input file without a time window.
- The tool does not block IP addresses or modify firewall rules.

**Future Improvements**

- Add command-line arguments for log file paths and alert thresholds.
- Validate extracted IP addresses.
- Support additional authentication log formats.
- Detect repeated failures within configurable time windows.
- Expand automated test coverage for alert generation.
