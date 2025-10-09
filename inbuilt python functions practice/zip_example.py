
#unique examples showing usage of Python's zip() function


# Example 1: Zip names and roll numbers
students = ["Ravi", "Neha", "Amit"]
rolls = [201, 202, 203]
for s, r in zip(students, rolls):
    print(s, "->", r)

# Example 2: Zip three iterables
marks = [88, 77, 93]
grades = ["A", "B", "A+"]
for s, m, g in zip(students, marks, grades):
    print(s, "got", m, "marks and grade", g)

# Example 3: Unequal lengths
projects = ["IoT", "AI"]
for s, p in zip(students, projects):
    print(s, "project:", p)

# Example 4: Unzipping
pairs = [("red", 1), ("blue", 2), ("green", 3)]
colors, ids = zip(*pairs)
print("Colors:", colors, "IDs:", ids)

# Example 5: Zipping strings
s1 = "abc"
s2 = "123"
print("Zipped strings:", list(zip(s1, s2)))

# Example 6: Creating dictionary with zip
keys = ["id", "name", "dept"]
values = [101, "Sita", "CSE"]
info = dict(zip(keys, values))
print("Dictionary:", info)

# Example 7: Iterating zipped list with enumerate
for idx, (s, m) in enumerate(zip(students, marks), start=1):
    print("Record", idx, ":", s, m)
