def password_strength(password):
    score = 0

    # Check for length
    if len(password) >= 8:
        score += 1

    # Check for uppercase and lowercase letters
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1

    # Check for numbers
    if any(char.isdigit() for char in password):
        score += 1

    # Check for special characters
    special_characters = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"
    if any(char in special_characters for char in password):
        score += 1

    return score


def password_feedback(password):
    score = password_strength(password)

    if score == 0:
        return "Your password is very weak. Please make it stronger by including a mix of uppercase and lowercase letters, numbers, and special characters."
    elif score == 1:
        return "Your password is weak. To make it stronger, include a mix of uppercase and lowercase letters, numbers, and special characters."
    elif score == 2:
        return "Your password is moderate. To make it stronger, include a mix of uppercase and lowercase letters, numbers, and special characters."
    elif score == 3:
        return "Your password is strong. However, to make it stronger, include a mix of uppercase and lowercase letters, numbers, and special characters."
    elif score == 4:
        return "Your password is very strong. Well done!"


# Test the functions
password = "Jeevan@1432"
feedback = password_feedback(password)
print(feedback)
