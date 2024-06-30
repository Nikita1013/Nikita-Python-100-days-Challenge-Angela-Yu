# Import logo, random 
import random
from art import logo , vs
# from art import vs
from game_data import data
import os


def get_random_account():
    return random.choice(data)


def format_data(account):
    # format the account data into printable format.
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess,a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

#Display the art
def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
    #  Use the randint() to generate random integer

        account_a = account_b
        account_b =random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)
            

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        # Ask user for the guess.
        guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
        #check if the user id correct
        # Get follower count to each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        guess_point = check_answer(guess, a_follower_count, b_follower_count)

        os.system('cls')
        print(logo)

        # use if statement to check if user is correct.
        # give user feedback on their guess.
        if guess_point:
            score +=1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, You got it wrong. Final score {score}")


game()

# give user feedback on their guess.

# Make the game repeatable.

# Making account at position B become the next account st position A


