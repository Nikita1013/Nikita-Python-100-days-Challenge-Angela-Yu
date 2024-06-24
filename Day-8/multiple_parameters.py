# functions with multiple parameters

# name = input("Enter your name: ")
# Positional Arguments
def greet_with_name(name,age):
    print(f"Hello! I'm {name}")
    print(f"My age is {age}??")

greet_with_name("Nikita", 22)


# Keyword Arguments
def greet_with_keywords(name,age,loc):
    print(f"Hello!! I'm {name}")
    print(f"My age is {age}")
    print(f"I am from {loc}")

greet_with_keywords(loc="S.Korea", age=27, name="Kookie")

