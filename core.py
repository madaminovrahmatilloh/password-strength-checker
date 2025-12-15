import re

COMMON_PASSWORDS = {
    "123456", "password", "qwerty", "admin123",
    "123456789", "iloveyou", "welcome"
}

def estimate_crack_time(password: str) -> str:
    length = len(password)

    if length < 6:
        return "Instantly (VERY weak)"
    elif length < 8:
        return "A few seconds"
    elif length < 9:
        return "A few minutes"
    elif length < 10:
        return "A few hours"
    else:
        return "Several years"


def check_strength_score(password: str) -> int:
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+\-\/]", password):
        score += 1

    return score


def analyze_password(password: str) -> dict:
    if password.lower() in COMMON_PASSWORDS:
        return {
            "strength": "Very Weak",
            "score": 0,
            "crack_time": "Instantly",
            "common": True
        }

    score = check_strength_score(password)

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "crack_time": estimate_crack_time(password),
        "common": False
    }
