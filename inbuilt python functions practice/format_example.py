

#unique examples showing usage of Python's str.format() method


# Example 1: Positional arguments
print("Welcome {}, your ticket number is {}.".format("Anjali", 145))

# Example 2: Keyword arguments
print("The {team} scored {runs} runs.".format(team="India", runs=325))

# Example 3: Formatting floating point numbers
speed = 123.456789
print("Train speed: {:.2f} km/h".format(speed))

# Example 4: Alignment
print("{:<12} | {:^12} | {:>12}".format("Left", "Center", "Right"))

# Example 5: Dictionary unpacking
student = {"name": "Vikram", "score": 89}
print("Student: {name}, Score: {score}".format(**student))

# Example 6: Number formatting with leading zeros
print("Invoice number: {:05}".format(42))

# Example 7: Using indices for reuse
print("{0} scored {1}, and again {0} improved to {2}".format("Arjun", 75, 88))
