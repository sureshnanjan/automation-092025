"""
Demonstrates how to use the zip() function to combine iterables.
"""

# Lists of names and ages
names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35, 40]
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']

# Combine two lists using zip
print("Names and Ages:")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# Combine three lists using zip
print("\nNames, Ages, and Cities:")
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age} years old, lives in {city}")

# Using zip to create a dictionary
name_age_dict = dict(zip(names, ages))
print("\nDictionary of Names and Ages:", name_age_dict)
