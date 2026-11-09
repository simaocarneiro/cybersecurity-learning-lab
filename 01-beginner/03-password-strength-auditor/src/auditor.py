
from pathlib import Path
import re

# Locate the sample password file relative to this script.
PASSWORD_FILE = (
    Path(__file__).resolve().parent.parent
    / "passwords"
    / "sample_passwords.txt"
)

COMMON_PATTERNS = [
    "password",
    "welcome",
    "qwerty",
    "admin",
    "abc123",
    "123456",
]

# Normalize common character substitutions.
LEET_TRANSLATION = str.maketrans({
    "0": "o",
    "1": "i",
    "3": "e",
    "4": "a",
    "5": "s",
    "7": "t",
    "@": "a",
    "$": "s",
})


def evaluate_password(password):
    score = 0
    recommendations = []

    # Check password length.
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        recommendations.append("Use at least 12 characters.")

    # Check character diversity.
    if re.search(r"[a-z]", password):
        score += 1
    else:
        recommendations.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        recommendations.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        recommendations.append("Add numbers.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        recommendations.append("Add special characters.")

    # Normalize common character substitutions.
    normalized_password = password.lower().translate(
        LEET_TRANSLATION
    )

    # Check for common or predictable patterns.
    if any(
        pattern in normalized_password
        for pattern in COMMON_PATTERNS
    ):
        score -= 2
        recommendations.append(
            "Avoid common words and predictable patterns."
        )

    # Assign a strength category.
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "recommendations": recommendations,
    }


def main():
    try:
        with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
            passwords = [
                line.strip()
                for line in file
                if line.strip()
            ]
    except FileNotFoundError:
        print(f"Error: Password file not found: {PASSWORD_FILE}")
        return

    print("=== Password Strength Auditor ===\n")

    for password in passwords:
        result = evaluate_password(password)

        print(f"Password: {password}")
        print(f"Strength: {result['strength']}")
        print(f"Score: {result['score']}")

        if result["recommendations"]:
            print("Recommendations:")
            for recommendation in result["recommendations"]:
                print(f"  - {recommendation}")
        else:
            print("Recommendations: None")

        print("-" * 40)


if __name__ == "__main__":
    main()
