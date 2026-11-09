import sys
import unittest
from pathlib import Path

# Import the monitor from the src directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from auditor import evaluate_password

class TestPasswordAuditor(unittest.TestCase):

    def test_weak_password(self):
        result = evaluate_password("password")
        self.assertEqual(result["strength"], "Weak")

    def test_moderate_password(self):
        result = evaluate_password("Summer2026")
        self.assertEqual(result["strength"], "Moderate")

    def test_strong_password(self):
        result = evaluate_password("Cyber!Secure2026")
        self.assertEqual(result["strength"], "Strong")

    def test_common_password_pattern(self):
        result = evaluate_password("P@ssw0rd")
        self.assertIn(
            "Avoid common words and predictable patterns.",
            result["recommendations"]
        )

    def test_short_password(self):
        result = evaluate_password("abc123")
        self.assertIn(
            "Use at least 12 characters.",
            result["recommendations"]
        )

if __name__ == "__main__":
    unittest.main()
