import random
from words import word_list
from Helper_Function import unique_characters_extractor, index_collector

# This section is for randomly fetching a word from words.py
word = random.choice(word_list)

while (word.isalpha() != True):
    word = random.choice(word_list)

# This section is to create an underscore list with the same length as of word
print_word = list("_" for _ in word)

# This section extracts unique characters from the string
# unique_characters = set(word)
unique_characters = unique_characters_extractor(word)

# already_guessed is an empty list which stores all the characters that have already been guessed by the user
already_guessed = []

# Printing the combined word
print("".join(print_word), "      (", print_word.count(
    "_"), "Letters! )")

# Initializing useful variables for conditions
hangman = "HANGMAN"
incorrect_guesses = 0

# Game Begins
while ("_" in print_word):

    # user_input stores the letter guessed by the user
    user_input = ""

    # Take user input while the guesssed letter is not a valid alphabet
    while not user_input.isalpha():
        print("Enter a valid alphabet between A - Z!")
        user_input = input("Guess the letter: ").lower()

    # If the guessed letter is correct and not already guessed then continue
    if user_input not in already_guessed and user_input in unique_characters:

        #  Push the guessed letter in the already guessed list and find its entries in the original word
        already_guessed.append(user_input)
        indices = index_collector(word, user_input)

        # Replace all the underscores with the entries of guessed letter
        for i in indices:
            print_word[i] = user_input+" "

    # If the guessed letter have already been guessed
    elif user_input in already_guessed:

        print(f"\nYou have already guessed the letter '{user_input}'")
        print("The letters you have already guessed are:")
        # Sort and display all the character that have already been guessed
        already_guessed.sort()
        print(already_guessed)
        print("\n", "".join(print_word), "      (", print_word.count(
            "_"), "letters left to guess)")

    # If the guessed letter is incorrect
    else:
        if (incorrect_guesses < 7):
            incorrect_guesses += 1
            already_guessed.append(user_input)
            print("Poor choice, Guess again!")
            print("\n", "".join(print_word), "      (", print_word.count(
                "_"), "letters left to guess)")
            print(hangman[: incorrect_guesses])
        else:
            print("\n\"YOU LOSE!\"")
            print(f"The word was \"{word}\"")
            break
else:
    print("\n\"YOU WON!\"")
    print(f"The word was \"{word}\"!")
