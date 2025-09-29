#!/usr/bin/env python3
"""
Python Introduction Tutorial for Entry-Level Learners
=====================================================

This file contains a structured introduction to Python programming concepts.
Each section builds upon the previous one, introducing concepts in logical order.

To run this file: python python_intro_tutorial.py

Author: Tutorial for Python Beginners
"""

# =============================================================================
# 1. BASIC PYTHON CONCEPTS
# =============================================================================

def section_1_basics():
    """
    Introduction to Python basics: variables, data types, and basic operations.
    
    Python is a high-level programming language that's easy to read and write.
    Variables store data, and Python has several built-in data types.
    """
    print("=== Section 1: Python Basics ===")
    
    # Variables - containers that store data values
    # Python automatically determines the type based on the value
    name = "Alice"           # String (text)
    age = 25                 # Integer (whole number)
    height = 5.6             # Float (decimal number)
    is_student = True        # Boolean (True/False)
    
    print(f"Name: {name} (type: {type(name).__name__})")
    print(f"Age: {age} (type: {type(age).__name__})")
    print(f"Height: {height} (type: {type(height).__name__})")
    print(f"Is student: {is_student} (type: {type(is_student).__name__})")
    
    # Basic arithmetic operations
    x, y = 10, 3
    print(f"\nArithmetic with {x} and {y}:")
    print(f"Addition: {x} + {y} = {x + y}")
    print(f"Subtraction: {x} - {y} = {x - y}")
    print(f"Multiplication: {x} * {y} = {x * y}")
    print(f"Division: {x} / {y} = {x / y}")
    print(f"Floor division: {x} // {y} = {x // y}")
    print(f"Modulus (remainder): {x} % {y} = {x % y}")
    print(f"Exponentiation: {x} ** {y} = {x ** y}")


# =============================================================================
# 2. STRINGS AND STRING OPERATIONS
# =============================================================================

def section_2_strings():
    """
    Working with strings - text data in Python.
    
    Strings are sequences of characters enclosed in quotes.
    Python provides many built-in methods for string manipulation.
    """
    print("\n=== Section 2: Strings ===")
    
    # Different ways to create strings
    single_quotes = 'Hello, World!'
    double_quotes = "Python Programming"
    triple_quotes = """This is a
    multi-line string"""
    
    # String operations
    first_name = "John"
    last_name = "Doe"
    
    # String concatenation
    full_name = first_name + " " + last_name
    print(f"Full name: {full_name}")
    
    # String formatting (f-strings - modern Python way)
    message = f"Hello, {first_name}! You are learning Python."
    print(message)
    
    # Useful string methods
    sample_text = "  Python is AWESOME!  "
    print(f"\nOriginal: '{sample_text}'")
    print(f"Lowercase: '{sample_text.lower()}'")
    print(f"Uppercase: '{sample_text.upper()}'")
    print(f"Stripped: '{sample_text.strip()}'")
    print(f"Replace: '{sample_text.replace('AWESOME', 'amazing')}'")
    
    # String slicing - extracting parts of strings
    word = "Programming"
    print(f"\nString slicing with '{word}':")
    print(f"First 4 characters: {word[:4]}")
    print(f"Last 3 characters: {word[-3:]}")
    print(f"Middle part: {word[2:7]}")


# =============================================================================
# 3. LISTS - ORDERED COLLECTIONS
# =============================================================================

def section_3_lists():
    """
    Lists are ordered, mutable collections that can store multiple items.
    
    Lists are one of the most versatile data structures in Python.
    They can contain different data types and can be modified after creation.
    """
    print("\n=== Section 3: Lists ===")
    
    # Creating lists
    fruits = ["apple", "banana", "orange", "grape"]
    numbers = [1, 2, 3, 4, 5]
    mixed_list = ["Alice", 25, True, 3.14]
    
    print(f"Fruits: {fruits}")
    print(f"Numbers: {numbers}")
    print(f"Mixed list: {mixed_list}")
    
    # Accessing list elements (indexing starts at 0)
    print(f"\nFirst fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    print(f"Second and third fruits: {fruits[1:3]}")
    
    # Modifying lists
    fruits.append("kiwi")  # Add to end
    print(f"After adding kiwi: {fruits}")
    
    fruits.insert(1, "mango")  # Insert at specific position
    print(f"After inserting mango: {fruits}")
    
    fruits.remove("banana")  # Remove specific item
    print(f"After removing banana: {fruits}")
    
    # List methods and properties
    print(f"\nList length: {len(fruits)}")
    print(f"Is 'apple' in fruits? {'apple' in fruits}")
    
    # List comprehensions - a Pythonic way to create lists
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares of 1-5: {squares}")


# =============================================================================
# 4. DICTIONARIES - KEY-VALUE PAIRS
# =============================================================================

def section_4_dictionaries():
    """
    Dictionaries store data in key-value pairs.
    
    Dictionaries are unordered, mutable collections where each value
    is accessed by its unique key rather than by index.
    """
    print("\n=== Section 4: Dictionaries ===")
    
    # Creating dictionaries
    student = {
        "name": "Alice Johnson",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.7,
        "graduated": False
    }
    
    print(f"Student info: {student}")
    
    # Accessing values
    print(f"\nStudent name: {student['name']}")
    print(f"Student age: {student.get('age')}")  # Safer way using .get()
    print(f"Student ID: {student.get('id', 'Not available')}")  # With default
    
    # Modifying dictionaries
    student["age"] = 21  # Update existing key
    student["email"] = "alice@email.com"  # Add new key-value pair
    print(f"\nUpdated student: {student}")
    
    # Dictionary methods
    print(f"\nAll keys: {list(student.keys())}")
    print(f"All values: {list(student.values())}")
    print(f"All items: {list(student.items())}")
    
    # Checking if key exists
    if "gpa" in student:
        print(f"GPA is available: {student['gpa']}")


# =============================================================================
# 5. CONTROL STRUCTURES - CONDITIONAL STATEMENTS
# =============================================================================

def section_5_conditionals():
    """
    Conditional statements allow programs to make decisions.
    
    if, elif, and else statements control program flow based on conditions.
    Python uses indentation to define code blocks.
    """
    print("\n=== Section 5: Conditional Statements ===")
    
    # Basic if-else
    age = 18
    print(f"Age: {age}")
    
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    
    # Multiple conditions with elif
    score = 85
    print(f"\nTest score: {score}")
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Letter grade: {grade}")
    
    # Logical operators
    temperature = 75
    is_sunny = True
    
    print(f"\nTemperature: {temperature}°F, Sunny: {is_sunny}")
    
    if temperature > 70 and is_sunny:
        print("Perfect weather for a picnic!")
    elif temperature > 70 or is_sunny:
        print("Good weather, but not perfect.")
    else:
        print("Not ideal weather for outdoor activities.")
    
    # Checking multiple conditions
    username = "alice"
    password = "secret123"
    
    if username == "alice" and password == "secret123":
        print(f"\nWelcome, {username}!")
    else:
        print("\nInvalid credentials.")


# =============================================================================
# 6. LOOPS - REPETITIVE EXECUTION
# =============================================================================

def section_6_loops():
    """
    Loops allow code to be executed repeatedly.
    
    Python has two main types of loops: 'for' and 'while'.
    'for' loops iterate over sequences, 'while' loops continue until a condition is false.
    """
    print("\n=== Section 6: Loops ===")
    
    # For loops - iterate over sequences
    print("For loop with list:")
    colors = ["red", "green", "blue", "yellow"]
    for color in colors:
        print(f"  Current color: {color}")
    
    # For loop with range
    print("\nFor loop with range:")
    for i in range(5):  # 0 to 4
        print(f"  Number: {i}")
    
    print("\nFor loop with range (1 to 5):")
    for i in range(1, 6):  # 1 to 5
        print(f"  Number: {i}")
    
    # For loop with enumerate (get index and value)
    print("\nFor loop with enumerate:")
    fruits = ["apple", "banana", "orange"]
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # While loops - continue until condition is false
    print("\nWhile loop:")
    count = 0
    while count < 3:
        print(f"  Count is: {count}")
        count += 1  # Same as count = count + 1
    
    # Loop control: break and continue
    print("\nLoop with break:")
    for i in range(10):
        if i == 3:
            break  # Exit the loop
        print(f"  i = {i}")
    
    print("\nLoop with continue:")
    for i in range(5):
        if i == 2:
            continue  # Skip this iteration
        print(f"  i = {i}")


# =============================================================================
# 7. FUNCTIONS - REUSABLE CODE BLOCKS
# =============================================================================

def section_7_functions():
    """
    Functions are reusable blocks of code that perform specific tasks.
    
    Functions help organize code, avoid repetition, and make programs
    more modular and easier to maintain.
    """
    print("\n=== Section 7: Functions ===")
    
    # Function definitions and calls are demonstrated here
    print("See the function definitions below for examples.")


def greet(name):
    """
    Simple function that greets a person.
    
    Args:
        name (str): The name of the person to greet
    
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Nice to meet you."


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    area = length * width
    return area


def get_grade(score):
    """
    Convert a numeric score to a letter grade.
    
    Args:
        score (int): Numeric score (0-100)
    
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def demonstrate_functions():
    """Demonstrate the use of the functions defined above."""
    print("\n--- Function Examples ---")
    
    # Using the greet function
    message = greet("Alice")
    print(message)
    
    # Using the calculate_area function
    room_area = calculate_area(12, 10)
    print(f"Room area: {room_area} square feet")
    
    # Using the get_grade function
    student_score = 87
    letter_grade = get_grade(student_score)
    print(f"Score {student_score} = Grade {letter_grade}")


def advanced_function_features():
    """
    Demonstrate advanced function features like default parameters
    and variable-length arguments.
    """
    print("\n--- Advanced Function Features ---")
    
    def greet_with_title(name, title="Mr./Ms."):
        """Function with default parameter."""
        return f"Hello, {title} {name}!"
    
    def calculate_total(*numbers):
        """Function with variable-length arguments."""
        return sum(numbers)
    
    def create_profile(**info):
        """Function with keyword arguments."""
        profile = "Profile:\n"
        for key, value in info.items():
            profile += f"  {key}: {value}\n"
        return profile
    
    # Demonstrate the functions
    print(greet_with_title("Smith"))
    print(greet_with_title("Johnson", "Dr."))
    
    total = calculate_total(1, 2, 3, 4, 5)
    print(f"Total of numbers: {total}")
    
    profile = create_profile(name="Alice", age=25, city="New York")
    print(profile)


# =============================================================================
# 8. ERROR HANDLING
# =============================================================================

def section_8_error_handling():
    """
    Error handling allows programs to gracefully handle unexpected situations.
    
    try-except blocks catch and handle errors without crashing the program.
    This is essential for creating robust applications.
    """
    print("\n=== Section 8: Error Handling ===")
    
    # Basic try-except
    print("Example 1: Handling division by zero")
    try:
        result = 10 / 0
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    
    # Handling multiple exception types
    print("\nExample 2: Handling multiple errors")
    def safe_divide(a, b):
        """Safely divide two numbers with error handling."""
        try:
            result = a / b
            return f"{a} / {b} = {result}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"
        except TypeError:
            return "Error: Please provide numbers only"
    
    print(safe_divide(10, 2))    # Normal case
    print(safe_divide(10, 0))    # Division by zero
    print(safe_divide(10, "a"))  # Type error
    
    # Try-except-else-finally
    print("\nExample 3: Complete error handling structure")
    def read_number():
        """Demonstrate try-except-else-finally."""
        try:
            # Simulate user input
            user_input = "25"  # This could be input() in real code
            number = int(user_input)
        except ValueError:
            print("That's not a valid number!")
            return None
        else:
            print("Successfully converted to number!")
            return number
        finally:
            print("This always executes (cleanup code goes here)")
    
    result = read_number()
    if result:
        print(f"The number you entered: {result}")


# =============================================================================
# 9. FILE OPERATIONS
# =============================================================================

def section_9_file_operations():
    """
    File operations allow programs to read from and write to files.
    
    Python provides built-in functions to work with files.
    Always use 'with' statements for proper file handling.
    """
    print("\n=== Section 9: File Operations ===")
    
    # Writing to a file
    filename = "sample_data.txt"
    
    print(f"Writing data to {filename}...")
    try:
        with open(filename, 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is a sample file.\n")
            file.write("Python file operations are easy!\n")
        print("✓ File written successfully!")
    
    except IOError as e:
        print(f"Error writing file: {e}")
        return
    
    # Reading from a file
    print(f"\nReading data from {filename}...")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
    except IOError as e:
        print(f"Error reading file: {e}")
    
    # Reading file line by line
    print("Reading file line by line:")
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                print(f"Line {line_number}: {line.strip()}")
    
    except IOError as e:
        print(f"Error reading file: {e}")
    
    # Working with CSV-like data
    data_to_write = [
        "Name,Age,City",
        "Alice,25,New York",
        "Bob,30,Los Angeles",
        "Charlie,22,Chicago"
    ]
    
    csv_filename = "people.csv"
    print(f"\nCreating CSV file: {csv_filename}")
    
    try:
        with open(csv_filename, 'w') as file:
            for line in data_to_write:
                file.write(line + '\n')
        
        # Read and process the CSV
        print("Reading CSV data:")
        with open(csv_filename, 'r') as file:
            lines = file.readlines()
            header = lines[0].strip().split(',')
            print(f"Headers: {header}")
            
            for line in lines[1:]:
                data = line.strip().split(',')
                person = dict(zip(header, data))
                print(f"Person: {person}")
    
    except IOError as e:
        print(f"Error with CSV operations: {e}")


# =============================================================================
# 10. OBJECT-ORIENTED PROGRAMMING BASICS
# =============================================================================

class Person:
    """
    A simple class representing a person.
    
    Classes are blueprints for creating objects. They encapsulate
    data (attributes) and functions (methods) that work on that data.
    """
    
    def __init__(self, name, age):
        """
        Initialize a new Person object.
        
        Args:
            name (str): The person's name
            age (int): The person's age
        """
        self.name = name
        self.age = age
    
    def introduce(self):
        """Return an introduction string."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        """Increase the person's age by 1."""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old."


class Student(Person):
    """
    A Student class that inherits from Person.
    
    Inheritance allows us to create specialized classes based on existing ones.
    Student has all Person features plus student-specific ones.
    """
    
    def __init__(self, name, age, student_id, major):
        """Initialize a Student object."""
        super().__init__(name, age)  # Call parent class constructor
        self.student_id = student_id
        self.major = major
        self.courses = []
    
    def enroll_course(self, course):
        """Enroll in a course."""
        self.courses.append(course)
        return f"{self.name} enrolled in {course}"
    
    def introduce(self):
        """Override parent method with student-specific introduction."""
        basic_intro = super().introduce()
        return f"{basic_intro} I'm studying {self.major}."


def section_10_oop():
    """
    Demonstrate object-oriented programming concepts.
    
    OOP helps organize code into reusable, maintainable structures
    that model real-world entities and their relationships.
    """
    print("\n=== Section 10: Object-Oriented Programming ===")
    
    # Creating and using objects
    print("Creating Person objects:")
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)
    
    print(person1.introduce())
    print(person2.introduce())
    
    # Calling methods
    print(f"\n{person1.have_birthday()}")
    
    # Creating Student objects (inheritance)
    print("\nCreating Student objects:")
    student1 = Student("Charlie", 20, "S12345", "Computer Science")
    print(student1.introduce())
    
    print(student1.enroll_course("Python Programming"))
    print(student1.enroll_course("Data Structures"))
    print(f"{student1.name}'s courses: {student1.courses}")


# =============================================================================
# 11. PRACTICAL EXAMPLES AND MINI-PROJECTS
# =============================================================================

def section_11_practical_examples():
    """
    Practical examples that combine multiple concepts learned.
    
    These examples show how different Python concepts work together
    to solve real-world problems.
    """
    print("\n=== Section 11: Practical Examples ===")
    
    # Example 1: Simple calculator
    def simple_calculator():
        """A basic calculator using functions and error handling."""
        print("\n--- Simple Calculator ---")
        
        def calculate(num1, num2, operation):
            """Perform calculation based on operation."""
            try:
                if operation == '+':
                    return num1 + num2
                elif operation == '-':
                    return num1 - num2
                elif operation == '*':
                    return num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        return "Error: Division by zero!"
                    return num1 / num2
                else:
                    return "Error: Invalid operation!"
            except Exception as e:
                return f"Error: {e}"
        
        # Example calculations
        operations = [
            (10, 5, '+'),
            (10, 3, '-'),
            (4, 7, '*'),
            (15, 3, '/'),
            (10, 0, '/'),  # Error case
        ]
        
        for num1, num2, op in operations:
            result = calculate(num1, num2, op)
            print(f"{num1} {op} {num2} = {result}")
    
    # Example 2: Word counter
    def word_counter():
        """Count words in a text string."""
        print("\n--- Word Counter ---")
        
        sample_text = """
        Python is a powerful programming language.
        It is easy to learn and versatile.
        Python is used in web development, data science, and automation.
        """
        
        # Clean and split the text
        words = sample_text.lower().replace('\n', ' ').split()
        word_count = {}
        
        # Count each word
        for word in words:
            # Remove punctuation
            clean_word = word.strip('.,!?";')
            if clean_word:
                word_count[clean_word] = word_count.get(clean_word, 0) + 1
        
        print(f"Total words: {len(words)}")
        print("Word frequencies:")
        
        # Sort by frequency (most common first)
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        
        for word, count in sorted_words[:10]:  # Show top 10
            print(f"  {word}: {count}")
    
    # Example 3: Simple data analysis
    def analyze_student_grades():
        """Analyze student grades using lists and dictionaries."""
        print("\n--- Student Grade Analysis ---")
        
        # Sample data
        students = [
            {"name": "Alice", "grades": [88, 92, 79, 93, 85]},
            {"name": "Bob", "grades": [75, 83, 91, 87, 88]},
            {"name": "Charlie", "grades": [92, 88, 84, 90, 86]},
            {"name": "Diana", "grades": [78, 85, 92, 88, 91]},
        ]
        
        print("Student Grade Report:")
        print("-" * 50)
        
        class_total = 0
        student_count = 0
        
        for student in students:
            name = student["name"]
            grades = student["grades"]
            
            average = sum(grades) / len(grades)
            highest = max(grades)
            lowest = min(grades)
            
            print(f"{name}:")
            print(f"  Grades: {grades}")
            print(f"  Average: {average:.1f}")
            print(f"  Highest: {highest}")
            print(f"  Lowest: {lowest}")
            print()
            
            class_total += average
            student_count += 1
        
        class_average = class_total / student_count
        print(f"Class Average: {class_average:.1f}")
    
    # Run all examples
    simple_calculator()
    word_counter()
    analyze_student_grades()


# =============================================================================
# 12. BEST PRACTICES AND TIPS
# =============================================================================

def section_12_best_practices():
    """
    Python best practices and coding tips for beginners.
    
    Following these practices will help you write better, more maintainable code.
    """
    print("\n=== Section 12: Best Practices ===")
    
    print("""
    Python Best Practices for Beginners:
    
    1. **Use descriptive variable names**
       ✓ Good: student_name, total_score, is_valid
       ✗ Avoid: x, data, temp, a1
    
    2. **Follow PEP 8 style guide**
       - Use 4 spaces for indentation
       - Keep lines under 80 characters
       - Use snake_case for variables and functions
       - Use UPPER_CASE for constants
    
    3. **Write docstrings for functions**
       - Explain what the function does
       - Document parameters and return values
       - Include usage examples when helpful
    
    4. **Handle errors gracefully**
       - Use try-except blocks for risky operations
       - Be specific about which errors you catch
       - Don't ignore errors silently
    
    5. **Keep functions small and focused**
       - One function should do one thing well
       - If a function is too long, break it into smaller functions
       - Functions should be easily testable
    
    6. **Use meaningful comments**
       - Explain WHY, not WHAT
       - Update comments when you change code
       - Don't over-comment obvious things
    
    7. **Be consistent**
       - Use the same naming conventions throughout
       - Follow the same code organization patterns
       - Be consistent with your error handling approach
    
    8. **Use Python idioms**
       - Use list comprehensions when appropriate
       - Use 'with' statements for file operations
       - Use 'in' for membership testing
       - Use enumerate() instead of manual counters
    
    9. **Test your code**
       - Test normal cases and edge cases
       - Use descriptive test names
       - Test one thing at a time
    
    10. **Keep learning**
        - Read other people's code
        - Practice regularly
        - Learn about Python standard library
        - Stay updated with Python best practices
    """)


# =============================================================================
# MAIN FUNCTION - RUNNING THE TUTORIAL
# =============================================================================

def main():
    """
    Main function that runs all tutorial sections.
    
    This function demonstrates the logical progression of Python concepts
    from basic syntax to practical applications.
    """
    print("Python Tutorial for Entry-Level Learners")
    print("=" * 50)
    print("This tutorial covers Python fundamentals step by step.")
    print("Each section builds upon the previous ones.\n")
    
    # Run all sections
    try:
        section_1_basics()
        section_2_strings()
        section_3_lists()
        section_4_dictionaries()
        section_5_conditionals()
        section_6_loops()
        section_7_functions()
        demonstrate_functions()
        advanced_function_features()
        section_8_error_handling()
        section_9_file_operations()
        section_10_oop()
        section_11_practical_examples()
        section_12_best_practices()
        
        print("\n" + "=" * 50)
        print("🎉 Congratulations! You've completed the Python tutorial!")
        print("Next steps:")
        print("- Practice by writing your own programs")
        print("- Explore Python libraries (requests, pandas, matplotlib)")
        print("- Build small projects to reinforce your learning")
        print("- Join Python communities and forums")
        
    except Exception as e:
        print(f"An error occurred while running the tutorial: {e}")
        print("Please check your Python installation and try again.")


# =============================================================================
# ADDITIONAL EXERCISES FOR PRACTICE
# =============================================================================

def bonus_exercises():
    """
    Additional exercises for students to practice.
    
    These exercises combine multiple concepts and encourage
    independent problem-solving.
    """
    print("\n=== Bonus Exercises ===")
    print("""
    Practice Exercises (Try these on your own!):
    
    1. **Number Guessing Game**
       - Generate a random number between 1-100
       - Ask user to guess the number
       - Provide hints (too high/too low)
       - Count the number of attempts
    
    2. **To-Do List Manager**
       - Create functions to add, remove, and display tasks
       - Save tasks to a file
       - Load tasks from a file when program starts
    
    3. **Simple Banking System**
       - Create Account class with deposit/withdraw methods
       - Implement balance checking and transaction history
       - Add error handling for invalid operations
    
    4. **Text Analyzer**
       - Read a text file
       - Count sentences, paragraphs, and average word length
       - Find the most common words
       - Calculate reading time estimate
    
    5. **Grade Calculator**
       - Input multiple assignment scores
       - Calculate weighted averages (tests vs homework)
       - Determine letter grade and GPA
       - Generate a grade report
    
    Tips for tackling these exercises:
    - Start simple and add features gradually
    - Break complex problems into smaller functions
    - Test each function separately
    - Don't be afraid to look up documentation
    - Practice makes perfect!
    """)


# =============================================================================
# 13. WORKING WITH MODULES AND PACKAGES
# =============================================================================

def section_13_modules():
    """
    Modules allow you to organize code into separate files and reuse functionality.
    
    Python's standard library contains many useful modules, and you can also
    create your own modules or install third-party packages.
    """
    print("\n=== Section 13: Modules and Packages ===")
    
    # Importing standard library modules
    import math
    import random
    import datetime
    from collections import Counter
    
    print("Using the math module:")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Pi value: {math.pi:.4f}")
    print(f"Cosine of 0: {math.cos(0)}")
    
    print("\nUsing the random module:")
    print(f"Random number (1-10): {random.randint(1, 10)}")
    print(f"Random choice from list: {random.choice(['apple', 'banana', 'orange'])}")
    
    # Shuffle a list
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print(f"Shuffled list: {numbers}")
    
    print("\nUsing the datetime module:")
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")
    print(f"Current year: {now.year}")
    
    # Create a specific date
    birthday = datetime.date(1990, 5, 15)
    print(f"Birthday: {birthday}")
    
    print("\nUsing the collections module:")
    text = "hello world hello python world"
    word_counts = Counter(text.split())
    print(f"Word counts: {word_counts}")
    print(f"Most common word: {word_counts.most_common(1)}")


def demonstrate_custom_module():
    """
    Demonstrate how to create and use custom functions as modules.
    
    In a real project, you would put these functions in separate .py files
    and import them into your main program.
    """
    print("\n--- Custom Module Example ---")
    
    # These functions could be in a file called 'utilities.py'
    def format_currency(amount):
        """Format a number as currency."""
        return f"${amount:.2f}"
    
    def calculate_tax(amount, tax_rate=0.08):
        """Calculate tax on an amount."""
        return amount * tax_rate
    
    def format_phone(phone_number):
        """Format a phone number string."""
        # Remove all non-digits
        digits = ''.join(filter(str.isdigit, phone_number))
        if len(digits) == 10:
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        return "Invalid phone number"
    
    # Using our "module" functions
    price = 29.99
    tax = calculate_tax(price)
    total = price + tax
    
    print(f"Price: {format_currency(price)}")
    print(f"Tax: {format_currency(tax)}")
    print(f"Total: {format_currency(total)}")
    
    phone = "1234567890"
    print(f"Formatted phone: {format_phone(phone)}")


# =============================================================================
# 14. LIST COMPREHENSIONS AND GENERATOR EXPRESSIONS
# =============================================================================

def section_14_comprehensions():
    """
    List comprehensions and generator expressions provide concise ways
    to create lists and iterate over data.
    
    These are powerful Python features that make code more readable
    and often more efficient.
    """
    print("\n=== Section 14: List Comprehensions ===")
    
    # Basic list comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Traditional way
    squares_traditional = []
    for num in numbers:
        squares_traditional.append(num ** 2)
    
    # List comprehension way
    squares_comprehension = [num ** 2 for num in numbers]
    
    print(f"Traditional squares: {squares_traditional}")
    print(f"Comprehension squares: {squares_comprehension}")
    
    # List comprehension with condition
    even_squares = [num ** 2 for num in numbers if num % 2 == 0]
    print(f"Even number squares: {even_squares}")
    
    # More complex list comprehensions
    words = ["python", "java", "javascript", "go", "rust"]
    
    # Get lengths of words longer than 4 characters
    long_word_lengths = [len(word) for word in words if len(word) > 4]
    print(f"Lengths of long words: {long_word_lengths}")
    
    # Convert to uppercase if starts with 'j'
    processed_words = [word.upper() if word.startswith('j') else word for word in words]
    print(f"Processed words: {processed_words}")
    
    # Dictionary comprehension
    word_lengths = {word: len(word) for word in words}
    print(f"Word lengths dict: {word_lengths}")
    
    # Set comprehension
    first_letters = {word[0] for word in words}
    print(f"First letters set: {first_letters}")
    
    # Nested list comprehension (2D list)
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"Multiplication matrix: {matrix}")
    
    # Generator expression (memory efficient)
    print("\nGenerator expressions:")
    large_numbers = (x ** 2 for x in range(1000000) if x % 1000 == 0)
    print(f"First 5 large squares: {list(next(large_numbers) for _ in range(5))}")


# =============================================================================
# 15. WORKING WITH DATES AND TIMES
# =============================================================================

def section_15_datetime():
    """
    Working with dates and times is common in many applications.
    
    Python's datetime module provides comprehensive tools for
    date and time manipulation.
    """
    print("\n=== Section 15: Dates and Times ===")
    
    import datetime
    
    # Current date and time
    now = datetime.datetime.now()
    today = datetime.date.today()
    current_time = datetime.time(now.hour, now.minute, now.second)
    
    print(f"Current datetime: {now}")
    print(f"Today's date: {today}")
    print(f"Current time: {current_time}")
    
    # Creating specific dates
    new_year = datetime.date(2024, 1, 1)
    meeting_time = datetime.datetime(2024, 3, 15, 14, 30)  # March 15, 2:30 PM
    
    print(f"\nNew Year 2024: {new_year}")
    print(f"Meeting time: {meeting_time}")
    
    # Date arithmetic
    one_week = datetime.timedelta(weeks=1)
    one_month_ago = today - datetime.timedelta(days=30)
    next_week = today + one_week
    
    print(f"\nOne month ago: {one_month_ago}")
    print(f"Next week: {next_week}")
    
    # Calculate age
    def calculate_age(birth_date):
        """Calculate age from birth date."""
        today = datetime.date.today()
        age = today.year - birth_date.year
        
        # Adjust if birthday hasn't occurred this year
        if today.month < birth_date.month or \
           (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        
        return age
    
    birth_date = datetime.date(1995, 8, 20)
    age = calculate_age(birth_date)
    print(f"\nBirth date: {birth_date}")
    print(f"Age: {age} years")
    
    # Format dates and times
    print(f"\nFormatted dates:")
    print(f"US format: {now.strftime('%m/%d/%Y')}")
    print(f"European format: {now.strftime('%d/%m/%Y')}")
    print(f"Long format: {now.strftime('%B %d, %Y')}")
    print(f"Time: {now.strftime('%I:%M %p')}")  # 12-hour format with AM/PM
    print(f"ISO format: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Parse date strings
    date_string = "2024-03-15"
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    print(f"\nParsed date from '{date_string}': {parsed_date.date()}")


# =============================================================================
# 16. REGULAR EXPRESSIONS (REGEX) BASICS
# =============================================================================

def section_16_regex():
    """
    Regular expressions are powerful tools for pattern matching in text.
    
    They're useful for validation, searching, and text processing tasks.
    """
    print("\n=== Section 16: Regular Expressions ===")
    
    import re
    
    # Basic pattern matching
    text = "The phone number is 555-123-4567 and email is john@example.com"
    
    # Find phone number
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        print(f"Found phone number: {phone_match.group()}")
    
    # Find email
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_match = re.search(email_pattern, text)
    if email_match:
        print(f"Found email: {email_match.group()}")
    
    # Validation functions
    def validate_email(email):
        """Validate email format using regex."""
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}
        return bool(re.match(pattern, email))
    
    def validate_phone(phone):
        """Validate US phone number format."""
        # Supports formats: (555) 123-4567, 555-123-4567, 5551234567
        pattern = r'^(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}
        return bool(re.match(pattern, phone))
    
    # Test validation
    emails = ["test@example.com", "invalid-email", "user@domain.co.uk"]
    phones = ["(555) 123-4567", "555-123-4567", "5551234567", "invalid"]
    
    print(f"\nEmail validation:")
    for email in emails:
        valid = validate_email(email)
        print(f"  {email}: {'✓' if valid else '✗'}")
    
    print(f"\nPhone validation:")
    for phone in phones:
        valid = validate_phone(phone)
        print(f"  {phone}: {'✓' if valid else '✗'}")
    
    # Text processing with regex
    def clean_text(text):
        """Clean text by removing extra spaces and special characters."""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters (keep letters, numbers, and basic punctuation)
        text = re.sub(r'[^A-Za-z0-9\s.,!?-]', '', text)
        return text.strip()
    
    messy_text = "  This   is    messy   text!!!   @#$%  Clean   it  up.  "
    cleaned = clean_text(messy_text)
    print(f"\nOriginal: '{messy_text}'")
    print(f"Cleaned: '{cleaned}'")


# =============================================================================
# 17. DEBUGGING AND TESTING
# =============================================================================

def section_17_debugging():
    """
    Debugging is the process of finding and fixing errors in code.
    
    Python provides several tools and techniques for debugging
    and testing your programs.
    """
    print("\n=== Section 17: Debugging and Testing ===")
    
    # Using print statements for debugging
    def calculate_average(numbers):
        """Calculate average with debug prints."""
        print(f"DEBUG: Input numbers: {numbers}")
        print(f"DEBUG: Number count: {len(numbers)}")
        
        if not numbers:
            print("DEBUG: Empty list detected!")
            return 0
        
        total = sum(numbers)
        print(f"DEBUG: Total sum: {total}")
        
        average = total / len(numbers)
        print(f"DEBUG: Calculated average: {average}")
        
        return average
    
    # Test the function
    test_numbers = [85, 92, 78, 96, 88]
    result = calculate_average(test_numbers)
    print(f"Average: {result}")
    
    # Assert statements for testing
    def test_calculator_functions():
        """Simple tests using assert statements."""
        print(f"\n--- Running Tests ---")
        
        def add(a, b):
            return a + b
        
        def multiply(a, b):
            return a * b
        
        def divide(a, b):
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        
        # Test cases
        try:
            # Test addition
            assert add(2, 3) == 5, "Addition test failed"
            assert add(-1, 1) == 0, "Addition with negative failed"
            print("✓ Addition tests passed")
            
            # Test multiplication
            assert multiply(4, 5) == 20, "Multiplication test failed"
            assert multiply(0, 100) == 0, "Multiplication by zero failed"
            print("✓ Multiplication tests passed")
            
            # Test division
            assert divide(10, 2) == 5, "Division test failed"
            assert abs(divide(1, 3) - 0.3333333333333333) < 1e-10, "Division precision failed"
            print("✓ Division tests passed")
            
            # Test error handling
            try:
                divide(5, 0)
                assert False, "Should have raised ValueError"
            except ValueError:
                print("✓ Error handling test passed")
            
            print("All tests passed! 🎉")
            
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    test_calculator_functions()
    
    # Common debugging techniques
    print(f"\n--- Debugging Tips ---")
    print("""
    Common Debugging Techniques:
    
    1. **Print statements**: Add print() calls to see variable values
    2. **Rubber duck debugging**: Explain your code line by line
    3. **Break complex expressions**: Split into smaller parts
    4. **Check your assumptions**: Use assert statements
    5. **Read error messages carefully**: They often point to the problem
    6. **Use descriptive variable names**: Makes debugging easier
    7. **Test small parts**: Test functions individually
    8. **Use a debugger**: Python's pdb module or IDE debugger
    
    Common Error Types:
    - SyntaxError: Invalid Python syntax
    - NameError: Variable not defined
    - TypeError: Wrong data type used
    - IndexError: List/string index out of range
    - KeyError: Dictionary key doesn't exist
    - AttributeError: Object doesn't have that method/attribute
    """)


# =============================================================================
# 18. PERFORMANCE AND OPTIMIZATION BASICS
# =============================================================================

def section_18_performance():
    """
    Understanding basic performance concepts helps write efficient code.
    
    While premature optimization should be avoided, knowing these concepts
    helps you make better design decisions.
    """
    print("\n=== Section 18: Performance Basics ===")
    
    import time
    
    # Timing code execution
    def time_function(func, *args, **kwargs):
        """Time how long a function takes to execute."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time
    
    # Compare different approaches
    def create_list_append(n):
        """Create list using append (slower for large lists)."""
        result = []
        for i in range(n):
            result.append(i ** 2)
        return result
    
    def create_list_comprehension(n):
        """Create list using list comprehension (faster)."""
        return [i ** 2 for i in range(n)]
    
    # Test performance
    n = 100000
    print(f"Creating list of {n} squares:")
    
    _, time1 = time_function(create_list_append, n)
    print(f"Append method: {time1:.4f} seconds")
    
    _, time2 = time_function(create_list_comprehension, n)
    print(f"List comprehension: {time2:.4f} seconds")
    
    if time1 > time2:
        improvement = ((time1 - time2) / time1) * 100
        print(f"List comprehension is {improvement:.1f}% faster")
    
    # Memory efficiency example
    def memory_efficient_processing():
        """Demonstrate generator vs list for memory efficiency."""
        print(f"\n--- Memory Efficiency ---")
        
        # Generator (memory efficient)
        def fibonacci_generator(n):
            """Generate fibonacci numbers up to n (memory efficient)."""
            a, b = 0, 1
            count = 0
            while count < n:
                yield a
                a, b = b, a + b
                count += 1
        
        # List version (uses more memory)
        def fibonacci_list(n):
            """Generate fibonacci numbers as list (uses more memory)."""
            result = []
            a, b = 0, 1
            for _ in range(n):
                result.append(a)
                a, b = b, a + b
            return result
        
        # Compare first 10 fibonacci numbers
        n = 10
        print(f"First {n} Fibonacci numbers:")
        
        # Using generator
        fib_gen = fibonacci_generator(n)
        print(f"Generator: {list(fib_gen)}")
        
        # Using list
        fib_list = fibonacci_list(n)
        print(f"List: {fib_list}")
        
        print("For large n, generator uses constant memory, list uses O(n) memory")
    
    memory_efficient_processing()
    
    # Performance tips
    print(f"\n--- Performance Tips ---")
    print("""
    Performance Best Practices:
    
    1. **Use appropriate data structures**:
       - Lists for ordered data you need to modify
       - Tuples for ordered data that won't change
       - Sets for unique items and fast membership testing
       - Dictionaries for key-value mappings
    
    2. **Avoid premature optimization**:
       - Write readable code first
       - Profile to find actual bottlenecks
       - Optimize only when necessary
    
    3. **Use built-in functions and libraries**:
       - Built-ins are usually faster (sum, max, min, etc.)
       - NumPy for numerical computations
       - Use appropriate algorithms and data structures
    
    4. **List comprehensions vs loops**:
       - List comprehensions are often faster
       - Generators for memory efficiency
       - Consider readability vs performance trade-offs
    
    5. **String operations**:
       - Use join() for multiple string concatenations
       - f-strings are efficient for formatting
       - Avoid repeated string concatenation in loops
    
    Remember: Readable code is often better than fast code!
    """)


# =============================================================================
# 19. FINAL PROJECT EXAMPLE
# =============================================================================

def section_19_final_project():
    """
    A comprehensive example that combines many concepts learned.
    
    This project demonstrates a simple personal expense tracker that
    uses classes, file I/O, error handling, and data analysis.
    """
    print("\n=== Section 19: Final Project - Expense Tracker ===")
    
    import json
    import datetime
    from collections import defaultdict
    
    class ExpenseTracker:
        """
        A simple expense tracking application.
        
        Features:
        - Add expenses with categories
        - View expenses by date range
        - Analyze spending by category
        - Save/load data to/from file
        """
        
        def __init__(self, filename="expenses.json"):
            """Initialize the expense tracker."""
            self.filename = filename
            self.expenses = []
            self.load_expenses()
        
        def add_expense(self, amount, description, category, date=None):
            """Add a new expense."""
            if date is None:
                date = datetime.date.today()
            
            expense = {
                'amount': float(amount),
                'description': description,
                'category': category,
                'date': date.isoformat() if hasattr(date, 'isoformat') else date
            }
            
            self.expenses.append(expense)
            print(f"✓ Added expense: {description} - ${amount:.2f}")
            return expense
        
        def get_expenses_by_date_range(self, start_date, end_date):
            """Get expenses within a date range."""
            filtered_expenses = []
            
            for expense in self.expenses:
                expense_date = datetime.datetime.strptime(
                    expense['date'], '%Y-%m-%d'
                ).date()
                
                if start_date <= expense_date <= end_date:
                    filtered_expenses.append(expense)
            
            return filtered_expenses
        
        def analyze_by_category(self):
            """Analyze expenses by category."""
            category_totals = defaultdict(float)
            
            for expense in self.expenses:
                category_totals[expense['category']] += expense['amount']
            
            return dict(category_totals)
        
        def get_monthly_summary(self, year, month):
            """Get summary for a specific month."""
            start_date = datetime.date(year, month, 1)
            
            # Get the last day of the month
            if month == 12:
                end_date = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
            else:
                end_date = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
            
            monthly_expenses = self.get_expenses_by_date_range(start_date, end_date)
            
            total = sum(expense['amount'] for expense in monthly_expenses)
            
            return {
                'expenses': monthly_expenses,
                'total': total,
                'count': len(monthly_expenses),
                'average': total / len(monthly_expenses) if monthly_expenses else 0
            }
        
        def save_expenses(self):
            """Save expenses to file."""
            try:
                with open(self.filename, 'w') as file:
                    json.dump(self.expenses, file, indent=2)
                print(f"✓ Expenses saved to {self.filename}")
            except Exception as e:
                print(f"❌ Error saving expenses: {e}")
        
        def load_expenses(self):
            """Load expenses from file."""
            try:
                with open(self.filename, 'r') as file:
                    self.expenses = json.load(file)
                print(f"✓ Loaded {len(self.expenses)} expenses from {self.filename}")
            except FileNotFoundError:
                print(f"No existing expense file found. Starting fresh.")
                self.expenses = []
            except Exception as e:
                print(f"❌ Error loading expenses: {e}")
                self.expenses = []
        
        def display_summary(self):
            """Display a summary of all expenses."""
            if not self.expenses:
                print("No expenses recorded yet.")
                return
            
            total_amount = sum(expense['amount'] for expense in self.expenses)
            category_analysis = self.analyze_by_category()
            
            print(f"\n--- Expense Summary ---")
            print(f"Total expenses: ${total_amount:.2f}")
            print(f"Number of transactions: {len(self.expenses)}")
            print(f"Average expense: ${total_amount/len(self.expenses):.2f}")
            
            print(f"\n--- By Category ---")
            for category, amount in sorted(category_analysis.items(), 
                                         key=lambda x: x[1], reverse=True):
                percentage = (amount / total_amount) * 100
                print(f"{category}: ${amount:.2f} ({percentage:.1f}%)")
    
    # Demonstrate the expense tracker
    print("Creating sample expense tracker...")
    tracker = ExpenseTracker("demo_expenses.json")
    
    # Add sample expenses
    sample_expenses = [
        (25.50, "Lunch at restaurant", "Food"),
        (60.00, "Gas for car", "Transportation"),
        (120.00, "Groceries", "Food"),
        (15.99, "Netflix subscription", "Entertainment"),
        (45.00, "Coffee and pastries", "Food"),
        (200.00, "Electric bill", "Utilities"),
        (35.00, "Movie tickets", "Entertainment"),
    ]
    
    for amount, desc, category in sample_expenses:
        tracker.add_expense(amount, desc, category)
    
    # Display analysis
    tracker.display_summary()
    
    # Monthly summary
    current_date = datetime.date.today()
    monthly_summary = tracker.get_monthly_summary(current_date.year, current_date.month)
    
    print(f"\n--- This Month's Summary ---")
    print(f"Total spent: ${monthly_summary['total']:.2f}")
    print(f"Number of transactions: {monthly_summary['count']}")
    print(f"Average per transaction: ${monthly_summary['average']:.2f}")
    
    # Save the data
    tracker.save_expenses()
    
    print(f"\n--- Project Features Demonstrated ---")
    print("""
    This expense tracker project demonstrates:
    ✓ Object-oriented programming (classes and methods)
    ✓ File I/O with JSON format
    ✓ Error handling with try-except blocks
    ✓ Date and time manipulation
    ✓ Data analysis and aggregation
    ✓ String formatting and user-friendly output
    ✓ Default parameters and optional arguments
    ✓ List comprehensions and built-in functions
    ✓ Documentation with docstrings
    ✓ Modular code organization
    """)


# =============================================================================
# 20. NEXT STEPS AND RESOURCES
# =============================================================================

def section_20_next_steps():
    """
    Guidance for continuing your Python learning journey.
    
    This section provides resources and recommendations for
    further Python development.
    """
    print("\n=== Section 20: Next Steps ===")
    
    print("""
    🎉 Congratulations on completing this Python tutorial!
    
    You've learned:
    • Python basics (variables, data types, operators)
    • Control structures (if/else, loops)
    • Functions and modules
    • Object-oriented programming basics
    • File handling and error management
    • Working with dates, regex, and comprehensions
    • Debugging and performance concepts
    • A complete project example
    
    === NEXT LEARNING STEPS ===
    
    1. **Practice Regularly**
       - Code every day, even if just for 15 minutes
       - Solve coding challenges on platforms like:
         • LeetCode (leetcode.com)
         • HackerRank (hackerrank.com)
         • Codewars (codewars.com)
         • Project Euler (projecteuler.net)
    
    2. **Build Projects**
       - Start with simple projects and gradually increase complexity
       - Project ideas:
         • Calculator with GUI
         • Web scraper for news/weather
         • Personal budget tracker
         • Simple web application with Flask
         • Data analysis with pandas
         • Automated email sender
         • Game (tic-tac-toe, snake, etc.)
    
    3. **Learn Popular Libraries**
       - **Web Development**: Flask, Django, FastAPI
       - **Data Science**: pandas, numpy, matplotlib, seaborn
       - **Machine Learning**: scikit-learn, tensorflow, pytorch
       - **GUI Development**: tkinter, PyQt, Kivy
       - **Web Scraping**: requests, BeautifulSoup, Scrapy
       - **Database**: SQLAlchemy, pymongo
       - **Testing**: pytest, unittest
    
    4. **Advanced Python Concepts**
       - Decorators and context managers
       - Generators and iterators
       - Async/await programming
       - Metaclasses and descriptors
       - Type hints and static typing
       - Design patterns
       - Performance optimization
    
    5. **Development Tools and Practices**
       - Version control with Git
       - Virtual environments (venv, conda)
       - Package management with pip
       - Code formatting (black, autopep8)
       - Linting (pylint, flake8)
       - IDE/Editor setup (VS Code, PyCharm)
       - Debugging tools
    
    6. **Join the Community**
       - Python.org official website
       - Reddit: r/Python, r/learnpython
       - Stack Overflow for Q&A
       - GitHub for open source projects
       - Local Python meetups and conferences
       - Discord/Slack Python communities
    
    7. **Recommended Books**
       - "Automate the Boring Stuff with Python" by Al Sweigart
       - "Python Crash Course" by Eric Matthes
       - "Effective Python" by Brett Slatkin
       - "Fluent Python" by Luciano Ramalho
    
    8. **Online Courses and Tutorials**
       - Python.org's official tutorial
       - Real Python (realpython.com)
       - Coursera Python courses
       - edX Python programs
       - YouTube Python channels
    
    === CAREER PATHS WITH PYTHON ===
    
    • **Web Developer**: Build websites and web applications
    • **Data Scientist**: Analyze data and build predictive models
    • **Software Engineer**: Develop applications and systems
    • **DevOps Engineer**: Automate deployment and infrastructure
    • **Machine Learning Engineer**: Build and deploy ML models
    • **Automation Engineer**: Automate repetitive tasks
    • **Research Scientist**: Use Python for scientific computing
    • **Game Developer**: Create games with Python
    
    === FINAL TIPS ===
    
    • Don't try to learn everything at once - focus on one area
    • Read other people's code to learn different approaches
    • Contribute to open source projects when ready
    • Document your learning journey (blog, GitHub)
    • Don't be afraid to make mistakes - they're learning opportunities
    • Stay curious and keep experimenting!
    
    Remember: Becoming proficient in Python (or any programming language)
    is a journey, not a destination. Keep practicing, stay curious, and
    enjoy the process of continuous learning!
    
    Good luck on your Python journey! 🐍✨
    """)


# Run the tutorial when script is executed directly
if __name__ == "__main__":
    main()
    section_13_modules()
    demonstrate_custom_module()
    section_14_comprehensions()
    section_15_datetime()
    section_16_regex()
    section_17_debugging()
    section_18_performance()
    section_19_final_project()
    section_20_next_steps()
    bonus_exercises