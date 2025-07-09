# Ask for the user's name
name = input("What is your name? ")

# Ask for the user's age (input returns a string, so we convert it)
age = int(input("How old are you now? "))

# Calculate age in 2050 (add 27 years)
future_age = age + 27

# Print personalized message
print("Hi", name + "!", "In 2050, you will be", future_age, "years old.")
