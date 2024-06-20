# W.A.P that works out whether if a given year is a leap year. 
#  A normal year has 365 days and lear year has 366 days a extra day in february
year = int( input("Which year do you want to check? \n"))

if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap year")
        else:
            print("Not Leap year")
    else: 
        print("Leap year")
else:
    print("Not Leap year")