#unique examples showing usage of Python's slice() function

numbers = [10, 20, 30, 40, 50, 60]

# Example 1: Slice with start and stop
s = slice(1, 4)
print("Slice [1:4]:", numbers[s])

# Example 2: Slice with step
s = slice(0, 6, 2)
print("Slice [0:6:2]:", numbers[s])

# Example 3: Slice only with stop
s = slice(3)
print("Slice [:3]:", numbers[s])

# Example 4: Slice with string
course = "PYTHONPROGRAMMING"
s = slice(2, 12, 3)
print("String slice [2:12:3]:", course[s])

# Example 5: Negative index slicing
print("Negative slice [-4:]:", numbers[-4:])

# Example 6: Reverse a list with slice
print("Reversed list:", numbers[::-1])

# Example 7: Slice on tuple
data = ("A", "B", "C", "D", "E")
print("Tuple slice [1:4]:", data[1:4])
