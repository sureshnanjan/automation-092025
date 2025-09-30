#unique examples showing usage of Python's enumerate() function


# Example 1: Basic enumerate with a list
subjects = ["Maths", "Physics", "Chemistry"]
for idx, sub in enumerate(subjects):
    print("Subject", idx, ":", sub)

# Example 2: Custom start index
for idx, sub in enumerate(subjects, start=100):
    print("Custom Index", idx, ":", sub)

# Example 3: Enumerate a tuple
sports = ("Cricket", "Football", "Tennis")
for idx, s in enumerate(sports, start=1):
    print("Sport", idx, ":", s)

# Example 4: Enumerate on string (characters)
text = "HELLO"
for idx, ch in enumerate(text):
    print("Character at", idx, ":", ch)

# Example 5: Convert enumerate object to list
countries = ["India", "USA", "Japan"]
print("List of tuples:", list(enumerate(countries, start=10)))

# Example 6: Create dictionary from enumerate
days = ["Mon", "Tue", "Wed"]
day_map = dict(enumerate(days, start=1))
print("Day dictionary:", day_map)

# Example 7: Enumerate with set (order may vary)
skills = {"Python", "C++", "Java"}
for idx, sk in enumerate(skills, start=50):
    print("Skill", idx, ":", sk)

