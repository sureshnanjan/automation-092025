"""
Demonstrates how to use filter() to filter elements in a list of strings.
"""

# List of words
words = ["apple", "banana", "cherry", "date", "kiwi", "mango"]

# Function to filter words longer than 5 characters
def long_words(word):
    return len(word) > 5

long_word_list = list(filter(long_words, words))
print("Words longer than 5 characters:", long_word_list)

# Function to filter words that start with 'a'
def starts_with_a(word):
    return word.startswith('a')

words_starting_with_a = list(filter(starts_with_a, words))
print("Words starting with 'a':", words_starting_with_a)

# Using lambda to filter words containing the letter 'e'
words_with_e = list(filter(lambda w: 'e' in w, words))
print("Words containing 'e':", words_with_e)

# Combining filter with upper() to get uppercase words longer than 4 letters
words_upper_long = list(map(str.upper, filter(lambda w: len(w) > 4, words)))
print("Uppercase words longer than 4 letters:", words_upper_long)
