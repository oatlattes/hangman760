import random

class Hangman: # Task 1: Create the Class
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []

    def check_guess(self, guess): #Task 2: Create methods for running the checks
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word): # Task 3: Define what happens if the letter is in the word
                if letter == guess:
                    self.word_guessed[i] = letter
            print(self.word_guessed)
            self.num_letters -= 1
        else: # Task 4: Define what happens if the letter is NOT in the word
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self): #Task 2: Create methods for running the checks
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