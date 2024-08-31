import random
from words import word_list


def index_collector(string, character):
    indices = []
    for index, char in enumerate(string):
        if char == character:
            indices.append(index)
        else:
            continue
    return indices


def print_word(word):
    print("".join(word), "      (", word.count("_"), "Letters! )")


# This section is for randomly fetching a word from words.py
# word = random.choice(word_list)

# while (word.isalpha() != True):
#     word = random.choice(word_list)
word = 'subtract'

# while True:
#     word = random.choice(word_list)
#     if word.isalpha():
#         break

# This section is to create an underscore list with the same length as of word
word_copy = list("_" * len(word))

# This section extracts unique characters from the string
# unique_characters = set(word)
unique_characters = set(word)

# Initialize an empty list which wil store all the characters that have already been guessed by the user
already_guessed_letters = []

# Printing the combined word
print_word(word_copy)

# Initializing useful variables for conditions
hangman = "HANGMAN"
incorrect_guesses = 0

# Game Begins
while ("_" in word_copy):

    # user_input stores the letter guessed by the user
    user_input = ""

    # Get valid user input (letters only)
    while not user_input.isalpha():
        user_input = input(
            "Guess the valid alphabet between (A - Z): ").lower()

    # Check if the guess is correct and new
    correct_guess = user_input in unique_characters
    new_guess = user_input not in already_guessed_letters

    if correct_guess and new_guess:
        #  Push the guessed letter in the already guessed list and find its entries in the original word
        already_guessed_letters.append(user_input)
        indices = index_collector(word, user_input)

        # Replace all the underscores with the entries of guessed letter
        for i in indices:
            word_copy[i] = user_input + " "

    # If the guessed letter have already been guessed
    elif (not new_guess):

        print(f"\nAlready guessed the letter '{user_input}'")
        print("The letters you have already guessed are:")
        # Sort and display all the character that have already been guessed
        print(sorted(already_guessed_letters))
        print_word(word_copy)

    # If the guessed letter is incorrect
    else:
        if (incorrect_guesses < 7):
            incorrect_guesses += 1
            already_guessed_letters.append(user_input)
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
