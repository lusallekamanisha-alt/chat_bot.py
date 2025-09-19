
name = input("What is your name? ")

print("Hello", name + "! Nice to meet you.)
feeling = input("How are you feeling today? ")

if feeling.lower() == "good":
    print("That's great to hear! Keep smiling, " + name + "!")
elif feeling.lower() == "bad":
    print("I'm sorry to hear that, " + name + ". I hope things get better soon.")
else:
    print("Thank you for sharing, " + name + ".")

