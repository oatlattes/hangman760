import random

favorite_fruits = ["banana", "blueberry", "mango", "peach", "orange"]
word_list = favorite_fruits

print(word_list) # Task 1 - Define the list of possible words

random_fruit = random.choice(word_list)
word = random_fruit

print(word) # Task 2 - Choose a random word from the list


guess = input("Please, enter a single letter:") # Task 3 - Asks the user for an input

if len(guess) == 1 and guess.isalpha(): # Task 4 - Check that the input is a single character
    print("Good guess!")

else:
    print("Oops! That is not a valid input.")

