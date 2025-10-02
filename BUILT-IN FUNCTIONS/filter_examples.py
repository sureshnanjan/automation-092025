# Demonstrates how to use the filter() function in Python

# filter(function, iterable)

# Example 1: Using filter with a named function
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print("Even numbers:", evens)

# Example 2: Using filter with lambda (anonymous function)
odds = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odds)

# Example 3: Filtering strings (keep only names starting with 'S')
names = ["Sowmya", "Ravi", "Suresh", "Meera"]
s_names = list(filter(lambda name: name.startswith("S"), names))
print("Names starting with S:", s_names)

# Example 4: Filter with None (removes falsy values: 0, '', False, None)
mixed = ["hello", "", 0, 42, None, "world"]
cleaned = list(filter(None, mixed))
print("After removing falsy values:", cleaned)
