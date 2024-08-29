import random
from words import word_list
from Helper_Function import unique_characters_extractor, index_collector

word = random.choice(word_list)

while (word.isalpha() != True):
    word = random.choice(word_list)

print_word = list("_" for _ in word)

unique_characters = unique_characters_extractor(word)

already_guessed = []
print("".join(print_word), "      (", print_word.count(
    "_"), "Letters! )")

hangman = "HANGMAN"
incorrect_guesses = 0

while ("_" in print_word):

    guess_character = input("Guess the letter: ").lower()

    while not guess_character.isalpha():
        print("Enter a valid alphabet between A - Z!")
        guess_character = input("Guess the letter: ").lower()

    if guess_character not in already_guessed and guess_character in unique_characters:

        already_guessed.append(guess_character)
        indices = index_collector(word, guess_character)

        for i in indices:
            print_word[i] = guess_character

    elif guess_character in already_guessed:

        print(f"\nYou have already guessed letter '{guess_character}'")
        print("The letters you have already guessed are:")
        already_guessed.sort()
        print(already_guessed)
        print("\n", "".join(print_word), "      (", print_word.count(
            "_"), "letters left to guess)")

    else:
        if (incorrect_guesses < 7):
            incorrect_guesses += 1
            already_guessed.append(guess_character)
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
