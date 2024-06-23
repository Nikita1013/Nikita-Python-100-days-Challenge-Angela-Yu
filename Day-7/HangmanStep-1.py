import random


# step -1 

word_list = ["ardvark","baboon","camel"]


#ToDo-1 Randomly  choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# Todo -2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

# Todo - 3 check if the letter the user guessed (guess) is one of the ltters in the chosen_word

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")