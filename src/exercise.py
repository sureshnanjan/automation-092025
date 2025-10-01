#Calculate BMI
def calculate_bmi(weight, height):
    bmi = weight/(height ** 2)
    return round(bmi, 2)


#Calculate fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 1)
print("Fahrenheit: " +str(celsius_to_fahrenheit(10)))

#Calculate compound interest
def compound_interest(principal, rate, years):
    r = rate / 100
    amount = principal * (1 + r) ** years
    return round(amount, 2)


#Count vowels
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)


#Reverse words
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])


#Palindrome
def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]
print("Second largest number: "+str(find_second_largest([5, 2, 8, 1, 9, 3])))

def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

#Merge dictionaries
def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged


#Group by length
def group_by_length(words):
    grouped = {}
    for word in words:
        length = len(word)
        grouped.setdefault(length, []).append(word)
    return grouped

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


#Calculate shipping cost
def calculate_shipping_cost(weight, distance, is_express):
    base_rate = 5
    weight_charge = weight * 2
    distance_charge = distance * 0.5
    cost = base_rate + weight_charge + distance_charge
    if is_express:
        cost *= 1.5  # add 50% surcharge
    return round(cost, 2)
