import string

def check_password_strength(password):
    """Checks the strength of a password based on various criteria."""

    # Define minimum password length
    min_length = 8

    # Check password length
    if len(password) < min_length:
        return f"Password must be at least {min_length} characters long."

    # Check for different character types
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    # print(string.punctuation)
    # Calculate password strength score
    score = 0
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Provide feedback based on score
    if score == 0:
        return "Very weak password. Use a combination of uppercase, lowercase, numbers, and special characters."
    elif score == 1 or score == 2:
        return "Weak password. Increase password length and use more character types."
    elif score == 3:
        return "Medium strength password. Consider adding more special characters."
    else:
        return "Strong password."

password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
