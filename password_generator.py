import random
import string

# Function to generate a random password
def generate_password(min_Length, numbers=True, special_characters=True):
    # Define possible character sets
    letters = string.ascii_letters        # a-z and A-Z
    digits = string.digits                # 0-9
    special = string.punctuation          # Special characters like !@#$%^&*

    # Start with letters, and add digits/specials if user wants them
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""                   # Password string
    meets_criteria = False     # Flag to check if all conditions are met
    has_number = False         # Tracks if at least one digit is included
    has_special = False        # Tracks if at least one special character is included

    # Keep generating characters until the password is long enough and meets criteria
    while not meets_criteria or len(pwd) < min_Length:
        new_char = random.choice(characters)  # Pick a random character
        pwd += new_char                       # Add to password

        # Check if the character is a digit
        if new_char in digits:
            has_number = True
        # Check if the character is a special symbol
        elif new_char in special:
            has_special = True

        # Check if password meets all criteria
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd  # Return the final password

# ---- Main program ----

# Ask user for the minimum length of the password
min_Length = int(input("Enter the minimum length: "))

# Ask user if they want numbers in the password
include_number = input("Do you want to have a number (y/n)? ").lower() == "y"

# Ask user if they want special characters in the password
include_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

# Generate password using user choices
pwd = generate_password(min_Length, include_number, include_special)

# Print the generated password
print(pwd)
