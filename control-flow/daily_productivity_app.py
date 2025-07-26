# Daily Productivity App

# --- Part 1: Mad Libs (Fun story generation) ---
print("\n--- Part 1: Create Your Fun Story ---")
name = input("Enter your name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")

print(f"\nOne day, {name} went to {place} and saw a {animal}.")
print(f"The {animal} looked at {name} and made them feel very {emotion}.")
print(f"{name} ran away as fast as they could, never looking back.")

# --- Part 2: Multiplication Table ---
print("\n--- Part 2: Productivity Boost Table ---")
number = int(input("Enter a number to boost your productivity: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

# --- Part 3: Motivational Pattern ---
print("\n--- Part 3: Motivational Pattern ---")
size = int(input("Enter the size of your motivation block: "))
row = 0

while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1

# --- Part 4: Task Reminder ---
print("\n--- Part 4: Daily Task Reminder ---")
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print(reminder)

print("\n✅ You're all set for the day. Stay productive!")
