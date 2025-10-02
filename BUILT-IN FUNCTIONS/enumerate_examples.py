# Demonstrates how to use the enumerate() function in Python

# enumerate() adds a counter (index) to an iterable like a list or string
fruits = ["apple", "banana", "cherry"]

# Example 1: Simple enumerate
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Example 2: Starting index from 1 instead of 0
for index, fruit in enumerate(fruits, start=1):
    print(f"Index starts at 1 -> {index}: {fruit}")

# Example 3: Enumerating a string (character by character)
for index, letter in enumerate("Python"):
    print(f"Character {letter} is at position {index}")
