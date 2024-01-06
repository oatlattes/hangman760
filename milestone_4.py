import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []

    def check_guess(self, guess): # Methods for running the checks
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word): # Defines what happens if the letter is in the word
                if letter == guess:
                    self.word_guessed[index] = letter
            print(self.word_guessed)
            self.num_letters -= 1
        else: # Defines what happens if the letter is NOT in the word
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self): # Methods for running the checks
         while True:
            guess = input("Guess the next letter: ")

            if not len(guess) == 1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list = ["banana", "blueberry", "mango", "peach", "orange"]
game = Hangman(word_list)
game.ask_for_input()