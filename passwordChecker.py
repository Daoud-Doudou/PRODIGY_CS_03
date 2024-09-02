import re

def password_check(password):
    criteria = {
        "length" : len(password) >= 8,
        "uppercase" : bool(re.search(r"[A-Z]", password)),
        "lowercase" : bool(re.search(r"[a-z]", password)),
        "numbers" : bool(re.search(r"\d",password)),
        "special_characters": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    strength = sum(criteria.values())

    feedback = []
    # Provide feedback for each criterion that is not met
    if not criteria["length"]:
        feedback.append("The password must be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("The password must contain at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("The password must contain at least one lowercase letter.")
    if not criteria["numbers"]:
        feedback.append("The password must contain at least one digit.")
    if not criteria["special_characters"]:
        feedback.append("The password must contain at least one special character.")


    # Determine the password strength level based on the number of criteria met
    if strength == 5:
        strength_level = "Strong"
    elif strength >= 3:
        strength_level = "Medium"
    else:
        strength_level = "Weak"

    return strength_level, feedback




def main():
    print("Checking the strength of your password")
    password = input("Enter your password: ")
    strength_level, feedback = password_check(password)
    
    # Print the strength level of the password
    print(f"Password Strength: {strength_level}")
    
    # Provide feedback if the password is not strong enough
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()