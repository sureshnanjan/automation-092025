#SECTION 1: BASICS - Variables and Operations

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

# SECTION 2: STRINGS

#Count vowels
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)
print(count_vowels("Hello World"))

#Reverse words
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])
print(reverse_words("Python is awesome"))