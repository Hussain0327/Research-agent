gooner = input("Are you a gooner? (yes/no): ").strip().lower()
if gooner == 'yes':
    print("Welcome fellow gooner!")
elif gooner == 'no':
    print("Oh, you're missing out on the Arsenal experience!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
content = input("Would you like some quality gooner content? (yes/no): ").strip().lower()
if content == 'yes':
    print("Great! Here's some exclusive gooner content just for you. Enjoy!")
    # Add your gooner content here
    print("1. Match Highlights")
    print("2. Player Interviews")
    print("3. Tactical Analysis")
elif content == 'no':
    print("No worries! Enjoy your day.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")