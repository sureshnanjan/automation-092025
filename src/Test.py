
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

def find_second_largest(numbers):
    unique = sorted(set(numbers), reverse=True)
    return unique[1] if len(unique) >= 2 else None
print(find_second_largest("1,3,14"))

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1,list2))


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

def invert_dictionary(d):
    return {v: k for k, v in d.items()}
original = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
swapped = invert_dictionary(original)
print(swapped)


def merge_dictionaries(dict1, dict2):

    merged = dict1.copy()
    for k, v in dict2.items():
        merged[k] = merged.get(k, 0) + v
    return merged
d1 = {'apple': 10, 'banana': 15}
d2 = {'banana': 7, 'cherry': 3}
result = merge_dictionaries(d1, d2)
print(result)

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

def categorize_temperature(temp_celsius):
    if temp_celsius <= 0:
        return "Freezing"
    elif 0 < temp_celsius <= 10:
        return "Cold"
    elif 10 < temp_celsius <= 20:
        return "Moderate"
    elif 20 < temp_celsius <= 30:
        return "Warm"
    else:
        return "Hot"


def triangle_type(a, b, c):
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
    base = 5
    cost = base + (2 * weight) + (0.5 * distance)
    if is_express:
        cost *= 1.5
    return round(cost, 2)

# =============================================================================
# SECTION 6: LOOPS
# =============================================================================

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fizzbuzz(n):
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
    return sum(int(d) for d in str(n))

# =============================================================================
# SECTION 7: FUNCTIONS
# =============================================================================

def find_prime_numbers(limit):

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
    return [item for sub in nested_list for item in sub]

# =============================================================================






