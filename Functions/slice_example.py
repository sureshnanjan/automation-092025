"""
Demonstrates how to use slice() to extract parts of a list.
"""

# List of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing using slice object
s = slice(2, 7)
print("Slice from index 2 to 6:", numbers[s])

# Slice with step
s = slice(1, 9, 2)  # start=1, stop=9, step=2
print("Slice from index 1 to 8 with step 2:", numbers[s])

# Negative indices
s = slice(-5, -1)  # last 5th to last 2nd
print("Slice using negative indices:", numbers[s])

# Using slice directly in list indexing
print("First 5 elements using slice directly:", numbers[:5])
print("Every 2nd element using slice directly:", numbers[::2])
