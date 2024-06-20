# Love Calculator
# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combine names and convert to lowercase
combined_name = name1 + name2
name_lower = combined_name.lower()

# Calculate the TRUE score
t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")
true = t + r + u + e

# Calculate the LOVE score
l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")
love = l + o + v + e

# Combine the scores to get the love score
love_score = int(str(true) + str(love))

# Output the result

if (love_score < 10) or  (love_score > 90):
    print(f"Your score is {love_score}, you go together like Coke and Mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
