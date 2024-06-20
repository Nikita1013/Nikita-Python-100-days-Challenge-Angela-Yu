print("Welcome to Treasure Island.")
print("your mission is to find the treasure.")

# ---------------------------------------------

choice1 = input('You\'re at a cross road. Where do you want to go ? Type "left" or "right" \n').lower()

if choice1 == "left":
    choice2 = input('You came to lake. There is an island in the middle of the lake. Type  "wait" to wait for a boat. Type "swim" to swim across \n').lower()
    if choice2 == "wait":
        choice3 = input("you arrived at the island unharmed. there is a house with 3 doors. One red, one yellow and one blue. which colour do you choose ? \n").lower()

        if  choice3 == "red":
            print("You entered a room of Fire. GAME OVER")
        elif choice3 == "blue":
            print("You entered a room of beasts. GAME OVER")
        elif choice3 == "yellow":
            print("------------------------YOU WON --------------------- \n" + "Great Choice!!! You have reached the safe room.")
        else:
            print("You choose a door that doesn't exist. GAME OVER")
    else:
        print("You got attacked by an angry trout. GAME OVER")
else:
    print("You fell into a hole. GAME OVER")