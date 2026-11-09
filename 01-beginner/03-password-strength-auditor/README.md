**Password Strenght Auditor**

*Overview*

The Password Strength Auditor is a Python-based educational tool designed to evaluate password characteristics using fictional sample passwords.

It analyzes password length, character diversity, and common predictable patterns to assign a basic strength classification and provide improvement recommendations.

**Objectives**

- Evaluate password length.
- Identify lowercase and uppercase letters
- Detect numericas and special characters.
- Recognize common words and predictable character substitutions.
- Classify passwords as Weak, Moderate, or Strong.
- Generate recommendations based on the evaluation results.
- Validate the evaluation logic through automated unit tests.

**Technologies**
- Python 3
- Regular Expressions (re)
- Unit Testing (unittest)
- Linux / Ubuntu

**Project Structure**

03-password-strength-auditor/
├── README.md
├── passwords/
│   └── sample_passwords.txt
├── src/
│   └── auditor.py
└── tests/
    └── test_auditor.py

**Usage**

Run the auditor from the project root:

   python3 src/auditor.py

The program reads fictional passwords samples from passwords/sample_passwords.txt and displays their classifications, scores, and recommendations.

**Example Output**

=== Password Strength Auditor ===

Password: password
Strength: Weak
Score: 0

**Automated Tests**

Run the test suite:

  python3 -m unittest discover -s tests -p "test_*.py" -v

The test suites validates:

- Weak password classification.
- Moderate password classification.
- Strong password classfication.
- Detection of common password patterns.
- Identification of insufficient password length.

*Test results:* 5 tests passed.

**Security Considerations**

- Only fictional sample passwords are used.
- Passwords are evaluated locally.
- No passwords are transmitted or stored externally.
- The scoring system is rule-based and intended for educational purposes.
- The classification is not a gaurantee of real-world password security.

**Limitations and Future Improvements**

- Implement more advanced password pattern detection.
- Improve password strength estimation.
- Add configurable evaluation policies.
- Expand automated test coverage.
- Improve handling of predictable sequences and repeated characters.

**Disclaimer**

This project is intended for educational purposes and demonstrates basic password evaluation techniques. It is not a replacement for professional password auditing tools or established password security standards.
