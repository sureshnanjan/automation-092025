"""
enumerate_example.py
Demonstrates how to use the enumerate() function in Python.
"""

# List of fruits
fruits = ['apple', 'banana', 'cherry', 'date']

# Using enumerate to loop with index
print("Using enumerate with default start (0):")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print("\nUsing enumerate with start index 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"Index {index}: {fruit}")

# Example with a condition: find index of fruit containing 'a'
print("\nFinding fruits that contain the letter 'a':")
for index, fruit in enumerate(fruits):
    if 'a' in fruit:
        print(f"Fruit {fruit} contains 'a' at index {index}")
