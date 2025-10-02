# Demonstrates how to use the zip() function in Python

names = ["Sowmya", "Shyam", "Sasikala"]
scores = [95, 88, 76]
subjects = ["Math", "Science", "English"]

# Example 1: Simple zip with 2 lists
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Example 2: Zip with 3 lists
for name, score, subject in zip(names, scores, subjects):
    print(f"{name} scored {score} in {subject}")

# Example 3: Converting zipped object to a list of tuples
zipped = list(zip(names, scores))
print("Zipped list of tuples:", zipped)

# Example 4: Unequal lengths (zip stops at the shortest iterable)
extra = [1, 2]
print("Zip stops at shortest:", list(zip(names, extra)))
