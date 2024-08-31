import random
from words import word_list


def print_word(word):
    print("".join(word), "\t(", word.count("_"), "Letters )")


# Randomly fetch a word from words.py
word = 'section'
# while True:
#     word = random.choice(word_list)
#     if word.isalpha():
#         break

# ------ Create an underscore list with the same length as of word ------
word_copy = list("_" * len(word))

# This section extracts unique characters from the word
unique_characters = set(word)

# Initialize an empty list which wil stores all the characters that have already been guessed by the user
already_guessed_letters = []

# Printing the combined word
print_word(word_copy)

# Initializing useful variables for conditions
hangman = "HANGMAN"
incorrect_guesses = 0

# Game Begins
while ("_" in word_copy):

    # guess stores the letter guessed by the user
    guess = ""

    # Get valid user input (letters only)
    while not guess.isalpha():
        guess = input(
            "Guess the valid alphabet between (A - Z): ").lower()

    # Check if the guess is correct and new
    correct_guess = guess in unique_characters
    new_guess = guess not in already_guessed_letters

    if correct_guess and new_guess:
        #  Push the guessed letter in the already guessed list and find its entries in the original word
        already_guessed_letters.append(guess)
        # indices = index_collector(word, guess)
        indices = [i for i, character in enumerate(
            word) if character == guess]

        # Replace all the underscores with the entries of guessed letter
        for i in indices:
            word_copy[i] = guess

    # If the guessed letter have already been guessed
    elif (not new_guess):

        print(f"\nAlready guessed the letter '{guess}'")
        print("The letters you have already guessed are:")
        # Sort and display all the character that have already been guessed
        print(sorted(already_guessed_letters))
        print_word(word_copy)

    # If the guessed letter is incorrect
    else:
        if (incorrect_guesses < 7):
            incorrect_guesses += 1
            already_guessed_letters.append(guess)
            print("Incorrect Guess!")
            print_word(word_copy)
            print(hangman[: incorrect_guesses])
        else:
            print("\n\"YOU LOSE!\"")
            print(f"The word was \"{word}\"")
            break
else:
    print("\n\"YOU WON!\"")
    print(f"The word was \"{word}\"!")
