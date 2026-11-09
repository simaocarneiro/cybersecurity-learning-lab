
import sys
import tempfile
import unittest
from pathlib import Path

# Import the analyzer from the src directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from analyzer import analyze_logs


class TestLogAnalyzer(unittest.TestCase):

    def analyze_sample(self, content):
        # Create a temporary log file for each test.
        with tempfile.TemporaryDirectory() as directory:
            log_path = Path(directory) / "auth.log"
            log_path.write_text(content, encoding="utf-8")
            return analyze_logs(log_path)

    def test_failed_attempts_by_ip(self):
        logs = (
            "Failed password for admin from 192.0.2.10 port 50001 ssh2\n"
            "Failed password for admin from 192.0.2.10 port 50002 ssh2\n"
            "Failed password for test from 192.0.2.30 port 50003 ssh2\n"
        )

        result = self.analyze_sample(logs)

        self.assertEqual(result["192.0.2.10"], 2)
        self.assertEqual(result["192.0.2.30"], 1)
        self.assertEqual(sum(result.values()), 3)

    def test_no_failed_attempts(self):
        result = self.analyze_sample("")

        self.assertEqual(sum(result.values()), 0)

    def test_successful_logins_are_ignored(self):
        logs = (
            "Accepted password for student from 192.0.2.20 port 50004 ssh2\n"
            "Accepted publickey for analyst from 192.0.2.50 port 50005 ssh2\n"
        )

        result = self.analyze_sample(logs)

        self.assertEqual(sum(result.values()), 0)


if __name__ == "__main__":
    unittest.main()
