"""
Demonstrates how to use the format() function for string formatting.
"""

# Basic formatting
name = "Alice"
age = 25
print("Hello using basic format():")
message = "My name is {} and I am {} years old.".format(name, age)
print(message)

# Numbered placeholders
print("\nUsing numbered placeholders:")
message = "I am {1} years old and my name is {0}.".format(name, age)
print(message)

# Named placeholders
print("\nUsing named placeholders:")
message = "My name is {n} and I am {a} years old.".format(n=name, a=age)
print(message)

# Formatting numbers
price = 49.98765
print("\nFormatting numbers with precision:")
print("Price: {:.2f}".format(price))  # 2 decimal places

# Align text
print("\nAlign text in columns:")
print("{:<10} {:>10}".format("Item", "Price"))
print("{:<10} {:>10.2f}".format("Book", 12.5))
print("{:<10} {:>10.2f}".format("Pen", 1.2))
