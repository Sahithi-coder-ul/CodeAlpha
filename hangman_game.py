import random

# Function to select a random word from a predefined list of words
def choose_random_word():
    # List of words for the game
    words = ["python", "hangman", "programming", "developer", "computer", "keyboard", "algorithm", "data"]
    # Randomly pick a word from the list
    return random.choice(words)

# Function to display the word with guessed letters revealed
def display_current_word(word, guessed_letters):
    # Create the word to be displayed with blanks for unguessed letters
    current_display = ""
    for letter in word:
        if letter in guessed_letters:
            current_display += letter  # Show the letter if guessed
        else:
            current_display += "_"  # Use underscore for unguessed letters
    return current_display

# Main Hangman game function
def play_hangman():
    # Step 1: Choose a random word for the game
    word_to_guess = choose_random_word()

    # Step 2: Initialize variables for the game
    guessed_letters = []  # This will store all guessed letters
    incorrect_guesses = 0  # This will track the number of incorrect guesses made
    max_incorrect_guesses = 6  # Maximum allowed incorrect guesses (6 chances)

    # Print the welcome message
    print("Welcome to Hangman!")
    print(f"Try to guess the word. You can make {max_incorrect_guesses} incorrect guesses.")
    print(display_current_word(word_to_guess, guessed_letters))  # Display the word with blanks

    # Step 3: Game loop - keep asking the player to guess until they win or lose
    while incorrect_guesses < max_incorrect_guesses:
        # Ask the player to input a guess (one letter at a time)
        guess = input("\nPlease guess a letter: ").lower()

        # Step 4: Validate the player's guess
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue  # Skip the rest of the loop if the input is invalid

        # Step 5: Check if the letter has been guessed before
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue  # Skip this guess and ask again

        # Step 6: Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Step 7: Check if the guess is in the word
        if guess in word_to_guess:
            print(f"Good job! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1  # Increment incorrect guesses counter
            print(f"Oops! The letter '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        # Step 8: Display the current state of the word
        print(display_current_word(word_to_guess, guessed_letters))

        # Step 9: Check if the player has guessed the whole word
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
            break  # End the game if the word is guessed correctly

    # Step 10: If the player runs out of guesses, the game is over
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nSorry, you've run out of guesses. The word was: {word_to_guess}")

# Step 11: Start the game
if __name__ == "__main__":
    play_hangman()
