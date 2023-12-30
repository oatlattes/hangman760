import random

favorite_fruits = ["banana", "blueberry", "mango", "peach", "orange"]
word_list = favorite_fruits

random_fruit = random.choice(word_list)
word = random_fruit

print(word)

guess = input("Please, enter a single letter:")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")

else:
    print("Oops! That is not a valid input.")

