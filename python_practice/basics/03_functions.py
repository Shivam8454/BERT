#!/usr/bin/env python3
"""
Exercise 3: Functions

Learn about defining and using functions in Python.
Complete the TODOs to practice function creation and usage.
"""

print("=== Exercise 3: Functions ===\n")

# TODO 1: Basic function definition
print("1. Basic Functions:")

# TODO: Define a function called 'greet' that takes a name parameter
# and returns a greeting string
def greet(name):
    # Your code here
    pass

# Test the function
# result = greet("Alice")
# print(f"Greeting: {result}")

# TODO 2: Function with multiple parameters
print(f"\n2. Multiple Parameters:")

# TODO: Define a function called 'calculate_area' that takes length and width
# and returns the area of a rectangle
def calculate_area(length, width):
    # Your code here
    pass

# Test the function
# area = calculate_area(5, 3)
# print(f"Rectangle area: {area}")

# TODO 3: Function with default parameters
print(f"\n3. Default Parameters:")

# TODO: Define a function called 'introduce' that takes name and age
# with age having a default value of 25
def introduce(name, age=25):
    # Your code here - return a string like "Hi, I'm Alice and I'm 30 years old"
    pass

# Test with and without age parameter
# print(introduce("Bob"))
# print(introduce("Charlie", 35))

# TODO 4: Function that returns multiple values
print(f"\n4. Multiple Return Values:")

# TODO: Define a function called 'get_stats' that takes a list of numbers
# and returns the minimum, maximum, and average
def get_stats(numbers):
    # Your code here - return min, max, average as a tuple
    pass

# Test the function
# numbers = [1, 5, 3, 9, 2, 7]
# min_val, max_val, avg_val = get_stats(numbers)
# print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val:.2f}")

# TODO 5: Function with *args (variable arguments)
print(f"\n5. Variable Arguments (*args):")

# TODO: Define a function called 'sum_all' that takes any number of arguments
# and returns their sum
def sum_all(*args):
    # Your code here
    pass

# Test with different numbers of arguments
# print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
# print(f"Sum of 10, 20: {sum_all(10, 20)}")
# print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")

# TODO 6: Function with **kwargs (keyword arguments)
print(f"\n6. Keyword Arguments (**kwargs):")

# TODO: Define a function called 'create_profile' that takes a name
# and any number of keyword arguments for additional profile info
def create_profile(name, **kwargs):
    # Your code here - create a dictionary with name and all kwargs
    pass

# Test the function
# profile1 = create_profile("Alice", age=25, city="New York")
# profile2 = create_profile("Bob", age=30, city="Boston", job="Developer")
# print(f"Profile 1: {profile1}")
# print(f"Profile 2: {profile2}")

# TODO 7: Recursive function
print(f"\n7. Recursion:")

# TODO: Define a recursive function called 'factorial' that calculates n!
def factorial(n):
    # Your code here
    # Base case: if n is 0 or 1, return 1
    # Recursive case: return n * factorial(n-1)
    pass

# Test factorial function
# print(f"5! = {factorial(5)}")
# print(f"0! = {factorial(0)}")

# TODO 8: Lambda functions
print(f"\n8. Lambda Functions:")

# TODO: Create lambda functions for:
# - Squaring a number
# - Adding two numbers
# - Checking if a number is even

square = None  # lambda x: your code here
add = None     # lambda x, y: your code here
is_even = None # lambda x: your code here

# Test lambda functions
# print(f"Square of 4: {square(4)}")
# print(f"Add 3 + 7: {add(3, 7)}")
# print(f"Is 6 even? {is_even(6)}")
# print(f"Is 7 even? {is_even(7)}")

# TODO 9: Function as parameter (Higher-order function)
print(f"\n9. Higher-Order Functions:")

# TODO: Define a function called 'apply_operation' that takes a list of numbers
# and a function, then applies the function to each number
def apply_operation(numbers, operation):
    # Your code here - use list comprehension or loop
    pass

# Test with lambda functions
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = apply_operation(numbers, lambda x: x ** 2)
# doubled_numbers = apply_operation(numbers, lambda x: x * 2)
# print(f"Original: {numbers}")
# print(f"Squared: {squared_numbers}")
# print(f"Doubled: {doubled_numbers}")

# TODO 10: Challenge - Function decorator (preview of advanced concepts)
print(f"\n10. Challenge - Simple Decorator:")

# TODO: Create a simple timing decorator function
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        # Your code here:
        # 1. Record start time
        # 2. Call the original function
        # 3. Record end time
        # 4. Print the execution time
        # 5. Return the function result
        pass
    return wrapper

# TODO: Apply the decorator to a function
@timer_decorator
def slow_function():
    """A function that takes some time to execute."""
    time.sleep(0.1)  # Sleep for 0.1 seconds
    return "Done!"

# Test the decorated function
# result = slow_function()
# print(f"Result: {result}")

print(f"\n✅ Exercise 3 complete! Check solutions/03_functions_solution.py")

# Self-test questions:
"""
1. What's the difference between parameters and arguments?
2. What happens if you don't return anything from a function?
3. Can a function call itself? What is this called?
4. What's the difference between *args and **kwargs?
5. When would you use a lambda function vs a regular function?
"""