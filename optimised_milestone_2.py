import random

def select_random_word(words):
    return random.choice(words)

def validate_guess(guess):  # Task 4 - Check that the input is a single character
    return len(guess) == 1 and guess.isalpha()

available_fruits = ["banana", "blueberry", "mango", "peach", "orange"]
available_words = available_fruits

print(available_words) # Task 1 - Define the list of possible words

select_word = select_random_word(available_words)
print(select_word) # Task 2 - Choose a random word from the list

user_guess = input("Please, enter a single letter:") # Task 3 - Asks the user for an input

if validate_guess(user_guess):
     print("Good guess!")

else:
    print("Oops! That is not a valid input.")
