
# Welcome message
print("Hey, we're just practicing today?")

# Ask for the user's name until a valid one is entered
name = ""
while not name.strip():
    if name != "":
        print("You didn't enter a name. Please try again.")
    name = input("What is your name? ")
name = name.strip().title()
print(f"Hello, {name}! It's great to meet you.\n")

# Math question loop
print("Let's do some basic math.")
while True:
    answer = input("What is 2 + 2? ").strip()
    if answer == "4":
        print(f"Correct, {name}! 2 + 2 is indeed 4.\n")
        break
    else:
        print("That's not quite right. Please try again.\n")

# Next section
print("Let's check if you're a gooner.")