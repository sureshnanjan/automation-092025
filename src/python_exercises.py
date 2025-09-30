"""
Python Proficiency Exercises
============================

This script contains implementations of Python exercises
covering basics, strings, lists, dictionaries, conditionals,
loops, functions, error handling, and object-oriented programming.

Author: Sivasree
Copyright (c) 2025 Sivasree
License: For educational and personal use only
"""

# =============================================================================
# SECTION 1: BASICS - Variables and Operations
# =============================================================================

def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index (BMI), rounded to 2 decimals."""
    return round(weight_kg / (height_m ** 2), 2)


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit, rounded to 1 decimal place."""
    return round((celsius * 9 / 5) + 32, 1)


def compound_interest(principal, rate, years):
    """Calculate compound interest rounded to 2 decimals."""
    amount = principal * ((1 + rate / 100) ** years)
    return round(amount, 2)


# =============================================================================
# SECTION 2: STRINGS
# =============================================================================

def count_vowels(text):
    """Count vowels (a, e, i, o, u) in a string (case insensitive)."""
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)


def reverse_words(sentence):
    """Reverse the order of words in a sentence."""
    return " ".join(sentence.split()[::-1])


def is_palindrome(text):
    """Check if text is palindrome (ignoring spaces/punctuation/case)."""
    import re
    cleaned = re.sub(r'[^a-z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]


# =============================================================================
# SECTION 3: LISTS
# =============================================================================

def find_second_largest(numbers):
    """Find second largest unique number in a list."""
    unique = sorted(set(numbers), reverse=True)
    return unique[1] if len(unique) >= 2 else None


def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into one sorted list."""
    return sorted(list1 + list2)


def remove_duplicates(items):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for i in items:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result


# =============================================================================
# SECTION 4: DICTIONARIES
# =============================================================================

def invert_dictionary(d):
    """Swap keys and values of a dictionary."""
    return {v: k for k, v in d.items()}


def merge_dictionaries(dict1, dict2):
    """Merge dictionaries and sum overlapping key values."""
    merged = dict1.copy()
    for k, v in dict2.items():
        merged[k] = merged.get(k, 0) + v
    return merged


def group_by_length(words):
    """Group words by their length."""
    result = {}
    for word in words:
        result.setdefault(len(word), []).append(word)
    return result


# =============================================================================
# SECTION 5: CONDITIONALS
# =============================================================================

def categorize_temperature(temp_celsius):
    """Categorize temperature into Freezing, Cold, Moderate, Warm, or Hot."""
    if temp_celsius < 0:
        return "Freezing"
    elif 0 <= temp_celsius <= 15:
        return "Cold"
    elif 16 <= temp_celsius <= 25:
        return "Moderate"
    elif 26 <= temp_celsius <= 35:
        return "Warm"
    else:
        return "Hot"


def check_triangle_type(a, b, c):
    """Check type of triangle or if it's invalid."""
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


def calculate_shipping_cost(weight, distance, is_express):
    """Calculate shipping cost based on weight, distance, and express flag."""
    base = 5
    cost = base + (2 * weight) + (0.5 * distance)
    if is_express:
        cost *= 1.5
    return round(cost, 2)


# =============================================================================
# SECTION 6: LOOPS
# =============================================================================

def factorial(n):
    """Calculate factorial of n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fizzbuzz(n):
    """Generate FizzBuzz sequence up to n."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def sum_of_digits(n):
    """Return sum of digits of n."""
    return sum(int(d) for d in str(n))


# =============================================================================
# SECTION 7: FUNCTIONS
# =============================================================================

def find_prime_numbers(limit):
    """Find all primes up to a given limit."""
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def calculate_statistics(numbers):
    """Return mean, median, min, max of a list of numbers."""
    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)
    mean = sum(numbers_sorted) / n
    if n % 2 == 1:
        median = numbers_sorted[n // 2]
    else:
        median = (numbers_sorted[n // 2 - 1] + numbers_sorted[n // 2]) / 2
    return {
        "mean": mean,
        "median": median,
        "min": min(numbers_sorted),
        "max": max(numbers_sorted),
    }


def flatten_list(nested_list):
    """Flatten a one-level nested list."""
    return [item for sub in nested_list for item in sub]


# =============================================================================
# SECTION 8: ERROR HANDLING
# =============================================================================

def safe_divide_with_default(a, b, default=0):
    """Safely divide, return default on error."""
    try:
        return a / b
    except Exception:
        return default


def parse_integer_list(string_list):
    """Parse integers from a list of strings, skipping invalids."""
    result = []
    for s in string_list:
        try:
            val = int(s)
            result.append(val)
        except ValueError:
            continue
    return result


def validate_age(age_string):
    """Validate and convert age string to int."""
    try:
        age = int(age_string)
    except ValueError:
        return (False, "Invalid age format")
    if 0 <= age <= 150:
        return (True, age)
    else:
        return (False, "Age out of valid range")


# =============================================================================
# SECTION 10: OOP
# =============================================================================

class BankAccount:
    """Simple BankAccount with deposit, withdraw, and history tracking."""
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions


class ShoppingCart:
    """ShoppingCart with add/remove items, totals, and discounts."""
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_total(self):
        return sum(info["price"] * info["quantity"] for info in self.items.values())

    def apply_discount(self, percentage):
        total = self.get_total()
        discount = total * (percentage / 100)
        return total - discount


class Rectangle:
    """Rectangle class supporting area, perimeter, square check, and comparisons."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()
