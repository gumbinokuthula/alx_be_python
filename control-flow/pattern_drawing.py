# Ask the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Start the row counter
row = 0

# Outer loop using while
while row < size:
    # Inner loop using for to print a row of asterisks
    for _ in range(size):
        print("*", end="")  # Print without newline
    print()  # Move to next line after a row is done
    row += 1  # Go to next row
