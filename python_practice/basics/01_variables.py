#!/usr/bin/env python3
"""
Exercise 1: Variables and Data Types

Learn about Python variables, data types, and basic operations.
Complete the TODOs below to practice working with different data types.
"""

# TODO 1: Create variables of different types
print("=== Exercise 1: Variables and Data Types ===\n")

# Create a string variable with your name
# TODO: Replace None with your name as a string
your_name = None

# Create an integer variable with your age
# TODO: Replace None with your age as an integer
your_age = None

# Create a float variable with your height in meters
# TODO: Replace None with your height as a float
your_height = None

# Create a boolean variable indicating if you like Python
# TODO: Replace None with True or False
likes_python = None

# TODO 2: Print variable information
print("Personal Information:")
print(f"Name: {your_name} (type: {type(your_name).__name__})")
print(f"Age: {your_age} (type: {type(your_age).__name__})")
print(f"Height: {your_height}m (type: {type(your_height).__name__})")
print(f"Likes Python: {likes_python} (type: {type(likes_python).__name__})")

# TODO 3: Perform basic operations
print(f"\nCalculations:")

# Calculate your birth year (current year - age)
# TODO: Replace None with the calculation
current_year = 2024
birth_year = None

# Calculate your height in centimeters
# TODO: Replace None with the calculation
height_cm = None

# Create a greeting message
# TODO: Replace None with a formatted string using your variables
greeting = None

print(f"Birth year: {birth_year}")
print(f"Height in cm: {height_cm}")
print(f"Greeting: {greeting}")

# TODO 4: Type conversion practice
print(f"\nType Conversions:")

# Convert your age to a string
age_str = str(your_age)
print(f"Age as string: '{age_str}' (type: {type(age_str).__name__})")

# Convert your height to an integer (rounds down)
height_int = int(your_height)
print(f"Height as integer: {height_int} (type: {type(height_int).__name__})")

# TODO 5: Challenge - Variable swapping
print(f"\nChallenge - Variable Swapping:")
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")

# TODO: Swap the values of a and b without using a third variable
# Hint: Use tuple unpacking -> a, b = b, a

print(f"After swap: a = {a}, b = {b}")

# Bonus: Multiple assignment
x, y, z = 1, 2, 3
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

print(f"\n✅ Exercise 1 complete! Check your solutions in solutions/01_variables_solution.py")

# Self-test questions (think about these):
"""
1. What happens if you try to add a string and an integer?
2. How can you check the type of a variable at runtime?
3. What's the difference between = and == in Python?
4. Can you change the value of a variable after it's created?
"""