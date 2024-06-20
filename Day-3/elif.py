print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))

if height >= 120:
    print("Yay!! you can ride Rollercoaster.")
    age = int(input("Enter your age : "))
    if age < 12:
        print("You need to pay $5")
    elif age <= 18:
        print("You need to pay $7")
    else:
        print("You need to pay $12")
else:
    print("Sorry you can't ride the rollercoaster")