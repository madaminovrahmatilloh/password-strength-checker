import re
import time

COMMON_PASSWORDS = {
    "123456", "password", "qwerty", "admin123",
    "123456789", "iloveyou", "welcome"
}

def estimate_crack_time(password):
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

def check_strength(password):
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

password = input("Enter a password: ")

if password.lower() in COMMON_PASSWORDS:
    print("\nThis is a very common password. Extremely weak!")
    time.sleep(1)

strength = check_strength(password)

print("\n--- Password Strength Report ---")

if strength <= 2:
    print("Weak password!")
elif strength == 3:
    print("Medium password!")
else:
    print("Strong password!")

print("Estimated crack time:",
estimate_crack_time(password))