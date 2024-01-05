import random

def select_random_word(words):
    return random.choice(words)

available_fruits = ["banana", "blueberry", "mango", "peach", "orange"]


select_word = select_random_word(available_fruits)
print(select_word)


def check_guess(guess): # Function to check the guessed letter
    guess = guess.lower()

    if guess in select_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input(select_word): # Function to ask for input
    while True:
        guess = input("Guess the next letter: ")
    
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")  
        else:
            break
    
    check_guess(guess)

ask_for_input(select_word)