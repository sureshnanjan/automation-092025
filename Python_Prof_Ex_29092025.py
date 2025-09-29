"""
Python Proficiency Exercises
============================

Complete these exercises to test your understanding of Python concepts.
Each section corresponds to topics covered in the tutorial.

Instructions:
- Implement each function according to its docstring
- Run pytest to validate your implementations
- All tests must pass to demonstrate proficiency
"""

# =============================================================================
# SECTION 1: BASICS - Variables and Operations
# =============================================================================

def calculate_bmi(weight_kg, height_m):
bmi = weight_kg / (height_m ** 2)
return round(bmi, 2)


def celsius_to_fahrenheit(celsius):
Convert_temp = (celsius * 9/5) + 32
return round(Convert_temp, 1)


def compound_interest(principal, rate, years):
r = rate/100
comp_int = principal * (1+r) ** years
return round(comp_int, 2)

# =============================================================================
# SECTION 2: STRINGS
# =============================================================================

def count_vowels(text):
vowels = "aeiou"
count = 0
    for char in text.lower():
        if char in vowels:
             count += 1
    return count