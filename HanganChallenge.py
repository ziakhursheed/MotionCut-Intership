import random

# List of words for the game
word_list = ['python', 'hangman', 'programming', 'developer', 'computer', 'data', 'science', 'algorithm']

def choose_word():
    """Choose a random word from the word list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Display the word with underscores for letters that have not been guessed."""
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    """Main function to run the hangman game."""
    print("Welcome to Hangman!")
    
    word = choose_word()  # Random word to guess
    guessed_letters = []  # Store the guessed letters
    attempts = 6          # Number of allowed incorrect guesses

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed Letters: {' '.join(guessed_letters)}")
        print(f"Remaining Attempts: {attempts}")

        guess = input("Guess a letter: ").lower()

        # Check if the input is a valid single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word '{word}' correctly.")
            break
    else:
        print(f"\nSorry, you're out of attempts. The correct word was '{word}'.")

# Start the game
hangman()
