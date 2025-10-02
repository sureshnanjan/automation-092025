# Demonstrates how to use the format() method in Python

# Example 1: Positional formatting
print("Hello {}, welcome to {}".format("Sowmya", "Python"))

# Example 2: Indexed formatting
print("I like {0} and {1}".format("tea", "coffee"))
print("I like {1} and {0}".format("tea", "coffee"))

# Example 3: Named placeholders
print("My name is {name} and I am learning {lang}".format(name="Suresh", lang="Python"))

# Example 4: Formatting numbers
print("The value of pi is approximately {:.2f}".format(3.14159))  # 2 decimal places
print("Binary of 10: {0:b}".format(10))  # binary
print("Hexadecimal of 255: {0:x}".format(255))  # hex

# Example 5: Aligning text
print("{:<10}".format("left"))    # left aligned
print("{:>10}".format("right"))   # right aligned
print("{:^10}".format("center"))  # centered
