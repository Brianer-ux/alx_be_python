# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to handle columns (printing stars in one row)
    for col in range(size):
        print("*", end="")
    # After finishing one row, move to the next line
    print()
    row += 1
