import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_characters=True):
    """Generate a random password based on the given options."""
    
    # Base set of characters (lowercase letters)
    characters = list(string.ascii_lowercase)
    
    # Optionally include uppercase letters, digits, and special characters
    if use_uppercase:
        characters.extend(string.ascii_uppercase)
    if use_digits:
        characters.extend(string.digits)
    if use_special_characters:
        characters.extend(string.punctuation)
    
    # Ensure password has at least one of each selected type of character
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special_characters:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password with random characters from the chosen set
    password.extend(random.choice(characters) for _ in range(length - len(password)))
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Welcome to the Random Password Generator!")
    
    try:
        # Get the desired password length from the user
        length = int(input("Enter the desired password length (minimum 6 characters): "))
        if length < 6:
            print("Password length should be at least 6 characters. Setting to 6.")
            length = 6
    except ValueError:
        print("Invalid input! Using default length of 8.")
        length = 8

    # Ask the user whether to include different types of characters
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_characters = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate and display the random password
    password = generate_password(length, use_uppercase, use_digits, use_special_characters)
    print(f"Generated password: {password}")

# Run the password generator
if __name__ == "__main__":
    main()
