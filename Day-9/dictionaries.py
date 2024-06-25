programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
    }


print(programming_dictionary["Bug"])

# Adding new entry to dictionary

programming_dictionary["Loop"] = "The action of doing something again and again."
# print(programming_dictionary)

# creating an empty dictionary
empty_dict = {}

# edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)


# Looping through dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


