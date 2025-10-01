
# =============================================================================
#SECTION 1: BASICS - Variables and Operations
# =============================================================================

#Calculate BMI
def calculate_bmi(weight, height):
    bmi = weight/(height ** 2)
    return round(bmi, 2)
print(calculate_bmi(70, 1.75))

#Calculate fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 1)
print(celsius_to_fahrenheit(10))

#Calculate compound interest
def compound_interest(principal, rate, years):
    r = rate / 100
    amount = principal * (1 + r) ** years
    return round(amount, 2)
print(compound_interest(1000, 5, 10))

# =============================================================================
# SECTION 2: STRINGS
# =============================================================================

#Count vowels
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)
print(count_vowels("Hello World"))

#Reverse words
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])
print(reverse_words("Python is awesome"))


# =============================================================================
# SECTION 3: LISTS
# =============================================================================
#Find second largest number
def find_second_largest(numbers):
    unique = sorted(set(numbers), reverse=True)
    return unique[1] if len(unique) >= 2 else None
print(find_second_largest("1,3,14"))

#Merge lists
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1,list2))

#Remove duplicates
def remove_duplicates(items):
    seen = set()
    result = []
    for i in items:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result
original_list = [3, 5, 2, 3, 7, 5, 2, 9]
print("Original list:", original_list)
cleaned_list = remove_duplicates(original_list)
print("List after removing duplicates:", cleaned_list)

# =============================================================================
# SECTION 4: DICTIONARIES
# =============================================================================
#Invert dictionaries
def invert_dictionary(d):
    return {v: k for k, v in d.items()}
original = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
swapped = invert_dictionary(original)
print(swapped)

#Merge dictionaries
def merge_dictionaries(dict1, dict2):

    merged = dict1.copy()
    for k, v in dict2.items():
        merged[k] = merged.get(k, 0) + v
    return merged
d1 = {'apple': 10, 'banana': 15}
d2 = {'banana': 7, 'cherry': 3}
result = merge_dictionaries(d1, d2)
print(result)

#Group by length
def group_by_length(words):
    result = {}
    for word in words:
        result.setdefault(len(word), []).append(word)
    return result
word_list = ["apple", "bat", "banana", "cat", "dog", "elephant"]
result = group_by_length(word_list)
print(result)

# =============================================================================
# SECTION 5: CONDITIONALS
# =============================================================================
#Categorize temperature
def categorize_temperature(temp_celsius):
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
print("Temperature: "+str(categorize_temperature(28)))

#Check triangle type
def check_triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
print("Triangle type: "+str(check_triangle_type(5, 5, 5)))

#Calculate shipping cost
def calculate_shipping_cost(weight, distance, is_express):
    base_rate = 5
    weight_charge = weight * 2
    distance_charge = distance * 0.5
    cost = base_rate + weight_charge + distance_charge
    if is_express:
        cost *= 1.5  # add 50% surcharge
    return round(cost, 2)
print("Shipping cost: "+str(calculate_shipping_cost(5, 100, False)))

# =============================================================================
# SECTION 6: LOOPS
# =============================================================================
#Factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print("Factorial number is: "+str(factorial(5)))

#Fizzbuzz
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
print(fizzbuzz(15))

#Sum of digits
def sum_of_digits(n):
    if n < 0:
        raise ValueError("Only non-negative integers are allowed .")
    return sum(int(digit) for digit in str(n))
print("Sum of digits: "+str(sum_of_digits(12345)))

# =============================================================================
# SECTION 7: FUNCTIONS
# =============================================================================

#Find prime numbers
def find_prime_numbers(limit):
    if limit < 2:
        return []
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Efficient check
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print("Prime numbers are: "+str(find_prime_numbers(25)))

#Calculate statistics numbers
def calculate_statistics(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mean = sum(numbers) / n
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2
    return {
        'mean': round(mean, 2),
        'median': median,
        'min': min(numbers),
        'max': max(numbers)
    }
print(calculate_statistics([1, 2, 3, 4, 5]))

#Flattened list
def flatten_list(nested_list):
    flattened = []
    for sublist in nested_list:
        flattened.extend(sublist)
    return flattened
print(flatten_list([[1, 2], [3, 4], [5, 6]]))
# =============================================================================
# SECTION 8: ERROR HANDLING
# =============================================================================
#Safe divide with default
def safe_divide_with_default(a, b, default=0):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return default
print(safe_divide_with_default(10, 3))
print(safe_divide_with_default(10, 0, -1))

#Parse integer list
def parse_integer_list(string_list):
    parsed = []
    for item in string_list:
        try:
            num = int(item)
            parsed.append(num)
        except ValueError:
            continue
    return parsed
print("Integers are: "+str(parse_integer_list(['1', '2', 'abc', '3', '4.5'])))

#Validate age
def validate_age(age_string):
    try:
        age = int(age_string)
        if 0 <= age <= 150:
            return True, age
        else:
            return False, "Age must be between 0 and 150"
    except ValueError:
        return False, "Invalid age format"
print("Valid age: "+str(validate_age('66')))
print("Invalid age: "+str(validate_age('abc')))
print("Invalid age: "+str(validate_age('234')))
# =============================================================================
# SECTION 10: OOP
# =============================================================================
#Calculate bank account
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = [f"Account opened with balance: {initial_balance}"]
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            return True
        return False
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            return True
        self.transaction_history.append(f"Failed withdrawal attempt: {amount}")
        return False
    def get_balance(self):
        return self.balance
    def get_transaction_history(self):
        return self.transaction_history
acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
print("Account balance: "+str(acc.get_balance()))
print("Transaction history :"+str(acc.get_transaction_history()))

#Shopping cart
class ShoppingCart:
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
        return round(sum(item["price"] * item["quantity"] for item in self.items.values()), 2)
    def apply_discount(self, percentage):
        if 0 <= percentage <= 100:
            discount = self.get_total() * (percentage / 100)
            return round(self.get_total() - discount, 2)
        return self.get_total()
cart = ShoppingCart()
cart.add_item("Book", 10.0, 2)
cart.add_item("Pen", 1.5, 3)
print("Total: "+str(cart.get_total()))
print("Discount :"+str(cart.apply_discount(10)))

#Calculate rectangle
class Rectangle:
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
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return NotImplemented
r1 = Rectangle(4, 5)
r2 = Rectangle(5, 5)
print("Area: "+str(r1.area()))
print(r2.is_square())
print(r1 < r2)







