#!/usr/bin/env python3
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
    """
    Calculate Body Mass Index (BMI).
    
    Formula: BMI = weight (kg) / height (m)^2
    
    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
    
    Returns:
        float: BMI value rounded to 2 decimal places
    
    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    pass


def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Formula: F = (C * 9/5) + 32
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit rounded to 1 decimal place
    
    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
    """
    pass


def compound_interest(principal, rate, years):
    """
    Calculate compound interest.
    
    Formula: A = P(1 + r)^t
    Where: A = final amount, P = principal, r = rate (as decimal), t = time
    
    Args:
        principal (float): Initial investment amount
        rate (float): Annual interest rate (as percentage, e.g., 5 for 5%)
        years (int): Number of years
    
    Returns:
        float: Final amount rounded to 2 decimal places
    
    Example:
        >>> compound_interest(1000, 5, 10)
        1628.89
    """
    pass


# =============================================================================
# SECTION 2: STRINGS
# =============================================================================

def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    Case insensitive.
    
    Args:
        text (str): Input string
    
    Returns:
        int: Number of vowels
    
    Example:
        >>> count_vowels("Hello World")
        3
    """
    pass


def reverse_words(sentence):
    """
    Reverse the order of words in a sentence.
    
    Args:
        sentence (str): Input sentence
    
    Returns:
        str: Sentence with words in reverse order
    
    Example:
        >>> reverse_words("Python is awesome")
        "awesome is Python"
    """
    pass


def is_palindrome(text):
    """
    Check if a string is a palindrome (reads same forwards and backwards).
    Ignore spaces, punctuation, and case.
    
    Args:
        text (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    
    Example:
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    pass


# =============================================================================
# SECTION 3: LISTS
# =============================================================================

def find_second_largest(numbers):
    """
    Find the second largest number in a list.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int/float: Second largest number, or None if list has fewer than 2 unique values
    
    Example:
        >>> find_second_largest([5, 2, 8, 1, 9, 3])
        8
    """
    pass


def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list
    
    Returns:
        list: Merged sorted list
    
    Example:
        >>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    pass


def remove_duplicates(items):
    """
    Remove duplicates from a list while preserving order.
    
    Args:
        items (list): List with potential duplicates
    
    Returns:
        list: List with duplicates removed, order preserved
    
    Example:
        >>> remove_duplicates([1, 2, 2, 3, 4, 3, 5])
        [1, 2, 3, 4, 5]
    """
    pass


# =============================================================================
# SECTION 4: DICTIONARIES
# =============================================================================

def invert_dictionary(d):
    """
    Invert a dictionary (swap keys and values).
    Assume all values are unique.
    
    Args:
        d (dict): Input dictionary
    
    Returns:
        dict: Inverted dictionary
    
    Example:
        >>> invert_dictionary({'a': 1, 'b': 2, 'c': 3})
        {1: 'a', 2: 'b', 3: 'c'}
    """
    pass


def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries. If keys overlap, sum their values.
    
    Args:
        dict1 (dict): First dictionary with numeric values
        dict2 (dict): Second dictionary with numeric values
    
    Returns:
        dict: Merged dictionary with summed values for overlapping keys
    
    Example:
        >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 5, 'c': 4}
    """
    pass


def group_by_length(words):
    """
    Group words by their length.
    
    Args:
        words (list): List of words
    
    Returns:
        dict: Dictionary where keys are lengths and values are lists of words
    
    Example:
        >>> group_by_length(['cat', 'dog', 'elephant', 'bee'])
        {3: ['cat', 'dog', 'bee'], 8: ['elephant']}
    """
    pass


# =============================================================================
# SECTION 5: CONDITIONALS
# =============================================================================

def categorize_temperature(temp_celsius):
    """
    Categorize temperature.
    
    Categories:
    - "Freezing": below 0
    - "Cold": 0-15
    - "Moderate": 16-25
    - "Warm": 26-35
    - "Hot": above 35
    
    Args:
        temp_celsius (float): Temperature in Celsius
    
    Returns:
        str: Temperature category
    
    Example:
        >>> categorize_temperature(20)
        "Moderate"
    """
    pass


def check_triangle_type(a, b, c):
    """
    Determine triangle type based on side lengths.
    
    Returns:
    - "Equilateral": all sides equal
    - "Isosceles": two sides equal
    - "Scalene": all sides different
    - "Not a triangle": if sides can't form a triangle
    
    Args:
        a, b, c (float): Side lengths
    
    Returns:
        str: Triangle type
    
    Example:
        >>> check_triangle_type(5, 5, 5)
        "Equilateral"
    """
    pass


def calculate_shipping_cost(weight, distance, is_express):
    """
    Calculate shipping cost based on weight, distance, and service type.
    
    Base rate: $5
    Weight charge: $2 per kg
    Distance charge: $0.50 per km
    Express surcharge: 50% extra
    
    Args:
        weight (float): Package weight in kg
        distance (float): Shipping distance in km
        is_express (bool): Whether express shipping
    
    Returns:
        float: Total shipping cost rounded to 2 decimal places
    
    Example:
        >>> calculate_shipping_cost(5, 100, False)
        65.0
    """
    pass


# =============================================================================
# SECTION 6: LOOPS
# =============================================================================

def factorial(n):
    """
    Calculate factorial of n using a loop.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    
    Example:
        >>> factorial(5)
        120
    """
    pass


def fizzbuzz(n):
    """
    Generate FizzBuzz sequence up to n.
    
    Rules:
    - Multiple of 3: "Fizz"
    - Multiple of 5: "Buzz"
    - Multiple of both: "FizzBuzz"
    - Otherwise: the number as string
    
    Args:
        n (int): Upper limit (inclusive)
    
    Returns:
        list: FizzBuzz sequence
    
    Example:
        >>> fizzbuzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
         '11', 'Fizz', '13', '14', 'FizzBuzz']
    """
    pass


def sum_of_digits(n):
    """
    Calculate sum of digits in a number.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Sum of digits
    
    Example:
        >>> sum_of_digits(12345)
        15
    """
    pass


# =============================================================================
# SECTION 7: FUNCTIONS
# =============================================================================

def find_prime_numbers(limit):
    """
    Find all prime numbers up to limit (inclusive).
    
    Args:
        limit (int): Upper limit
    
    Returns:
        list: List of prime numbers
    
    Example:
        >>> find_prime_numbers(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    pass


def calculate_statistics(numbers):
    """
    Calculate basic statistics for a list of numbers.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        dict: Dictionary with 'mean', 'median', 'min', 'max'
    
    Example:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'mean': 3.0, 'median': 3, 'min': 1, 'max': 5}
    """
    pass


def flatten_list(nested_list):
    """
    Flatten a nested list (one level deep).
    
    Args:
        nested_list (list): List containing lists
    
    Returns:
        list: Flattened list
    
    Example:
        >>> flatten_list([[1, 2], [3, 4], [5, 6]])
        [1, 2, 3, 4, 5, 6]
    """
    pass


# =============================================================================
# SECTION 8: ERROR HANDLING
# =============================================================================

def safe_divide_with_default(a, b, default=0):
    """
    Safely divide two numbers, returning default value on error.
    
    Args:
        a: Numerator
        b: Denominator
        default: Default value to return on error
    
    Returns:
        float: Result of division or default value
    
    Example:
        >>> safe_divide_with_default(10, 2)
        5.0
        >>> safe_divide_with_default(10, 0, -1)
        -1
    """
    pass


def parse_integer_list(string_list):
    """
    Parse a list of strings to integers, skipping invalid entries.
    
    Args:
        string_list (list): List of strings
    
    Returns:
        list: List of successfully parsed integers
    
    Example:
        >>> parse_integer_list(['1', '2', 'abc', '3', '4.5'])
        [1, 2, 3]
    """
    pass


def validate_age(age_string):
    """
    Validate and convert age string to integer.
    
    Requirements:
    - Must be convertible to integer
    - Must be between 0 and 150 (inclusive)
    
    Args:
        age_string (str): Age as string
    
    Returns:
        tuple: (is_valid, age_or_error_message)
    
    Example:
        >>> validate_age('25')
        (True, 25)
        >>> validate_age('abc')
        (False, 'Invalid age format')
    """
    pass


# =============================================================================
# SECTION 10: OOP
# =============================================================================

class BankAccount:
    """
    A simple bank account class.
    
    Requirements:
    - Track account holder name and balance
    - Support deposit and withdraw operations
    - Prevent overdrafts (balance cannot go negative)
    - Track transaction history
    """
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize bank account."""
        pass
    
    def deposit(self, amount):
        """
        Deposit money into account.
        
        Args:
            amount (float): Amount to deposit (must be positive)
        
        Returns:
            bool: True if successful, False otherwise
        """
        pass
    
    def withdraw(self, amount):
        """
        Withdraw money from account.
        
        Args:
            amount (float): Amount to withdraw (must be positive)
        
        Returns:
            bool: True if successful, False if insufficient funds
        """
        pass
    
    def get_balance(self):
        """
        Get current balance.
        
        Returns:
            float: Current balance
        """
        pass
    
    def get_transaction_history(self):
        """
        Get transaction history.
        
        Returns:
            list: List of transaction strings
        """
        pass


class ShoppingCart:
    """
    A shopping cart class.
    
    Requirements:
    - Add items with name, price, and quantity
    - Remove items
    - Calculate total cost
    - Apply discount codes
    """
    
    def __init__(self):
        """Initialize empty shopping cart."""
        pass
    
    def add_item(self, name, price, quantity=1):
        """Add item to cart."""
        pass
    
    def remove_item(self, name):
        """Remove item from cart."""
        pass
    
    def get_total(self):
        """
        Calculate total cost.
        
        Returns:
            float: Total cost
        """
        pass
    
    def apply_discount(self, percentage):
        """
        Apply discount to total.
        
        Args:
            percentage (float): Discount percentage (0-100)
        
        Returns:
            float: Discounted total
        """
        pass


class Rectangle:
    """
    A rectangle class with area and perimeter calculations.
    
    Requirements:
    - Store width and height
    - Calculate area and perimeter
    - Support comparison based on area
    """
    
    def __init__(self, width, height):
        """Initialize rectangle."""
        pass
    
    def area(self):
        """Calculate area."""
        pass
    
    def perimeter(self):
        """Calculate perimeter."""
        pass
    
    def is_square(self):
        """Check if rectangle is a square."""
        pass
    
    def __eq__(self, other):
        """Check if two rectangles have equal areas."""
        pass
    
    def __lt__(self, other):
        """Check if this rectangle has smaller area than other."""
        pass