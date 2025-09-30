
#unique examples showing usage of Python's filter() function


nums = [11, 24, 35, 40, 53]

# Example 1: Filter odd numbers
def is_odd(n):
    return n % 2 != 0
print("Odd numbers:", list(filter(is_odd, nums)))

# Example 2: Filter with lambda (multiples of 5)
print("Multiples of 5:", list(filter(lambda x: x % 5 == 0, nums)))

# Example 3: Filtering names starting with 'S'
names = ["Siva", "Arun", "Swathi", "Meena"]
print("Names starting with S:", list(filter(lambda n: n.startswith("S"), names)))

# Example 4: Removing empty values
items = ["hello", "", "python", None, "AI", 0]
print("Valid items:", list(filter(None, items)))

# Example 5: Filter positive numbers
values = [-3, -1, 0, 2, 5]
print("Positive numbers:", list(filter(lambda x: x > 0, values)))

# Example 6: Filter strings longer than 5 characters
words = ["pen", "notebook", "book", "encyclopedia"]
print("Long words:", list(filter(lambda w: len(w) > 5, words)))

# Example 7: Filter even squares
squares = [n * n for n in range(1, 11)]
print("Even squares:", list(filter(lambda x: x % 2 == 0, squares)))

