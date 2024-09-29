import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the number of allowed guesses
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get the user's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Make a guess: "))
            
            # Increase the attempt count
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Start the game
number_guessing_game()