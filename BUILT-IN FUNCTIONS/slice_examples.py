# Demonstrates how to use the slice() function in Python

# slice(start, stop, step)

# Example 1: Basic slicing on a list
nums = [0, 1, 2, 3, 4, 5, 6]
print(nums[slice(2, 5)])  # elements at index 2 to 4

# Example 2: Slice with step
print(nums[slice(1, 7, 2)])  # every 2nd element from index 1 to 6

# Example 3: Slice a string
word = "PythonProgramming"
print(word[slice(0, 6)])  # "Python"

# Example 4: Omitting start/stop
print(nums[slice(None, 4)])  # first 4 elements
print(nums[slice(3, None)])  # from index 3 till end

# Example 5: Negative indices
print(nums[slice(-4, -1)])  # elements near the end
