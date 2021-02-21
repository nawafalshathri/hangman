import random
import time
import json

# creates a hidden word
def create_blank_word(word):
    result = ''
    for i in range(len(word)):
        result += "_"
    return result

# updates count of guesses right or wrong
def guess_letter(word, letter):
    count = 0
    for let in word:
        if let == letter:
            count += 1
    return count

# prints the hangman
def print_hangman(number_of_wrong_guesses):
    hangman = ['''
          +---+
          |   |
              |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''']

    if (number_of_wrong_guesses >= len(hangman)):
        print("error, too many wrong guesses!")
    else:
        print(hangman[number_of_wrong_guesses])


# returns the bag of words
def get_bag_of_words():

    with open('words_dictionary.json') as f:
        data = json.load(f)
    return data

# updates the hidden word with the correct letters guessed
def update_hidden_word(hiddenword, letter, word):

    hiddenword = list(hiddenword)
    for i in range(len(hiddenword)):
        if letter == word[i]:
            hiddenword[i] = letter
        else:
            continue
    return "".join(hiddenword)

# runs the hangman game
def hangman_game():
    guessed = []
    bag_of_words = get_bag_of_words()

    random_word = random.choice(list(bag_of_words.keys()))
    #random_word = "bruh"
    num_wrong_guesses = 0

    num_right_guesses = 0

    hidden_word = create_blank_word(random_word)

    while(num_wrong_guesses < 7 and num_right_guesses != len(random_word)):


        print_hangman(num_wrong_guesses)

        print(hidden_word)


        keep_guessing = True

        print("Guess a letter: ")
        letter_guessed = input().lower()
        while(True):

            if (letter_guessed in guessed):
                print("Error! You already tried that!")
                time.sleep(0.3)
                print("Please try again")
                letter_guessed = input().lower()
                continue
            else:
                break

        guessed.append(letter_guessed)


        if guess_letter(random_word, letter_guessed) > 0:

                num_right_guesses += guess_letter(random_word, letter_guessed)
                hidden_word = update_hidden_word(hidden_word, letter_guessed, random_word)
                print(f"good job! you guessed {num_right_guesses} letters correct!")


        else:

            print("wrong guess!")
            num_wrong_guesses += 1

    if num_right_guesses == len(random_word):

        time.sleep(2)
        print("Congratulations! You Won!")

    else:
        time.sleep(1)
        print("Oh no! you lost!")

        time.sleep(1)
        print(f"The correct word was: {random_word}")

hangman_game()







