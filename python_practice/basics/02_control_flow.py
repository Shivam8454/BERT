#!/usr/bin/env python3
"""
Exercise 2: Control Flow (if/else, loops)

Learn about conditional statements and loops in Python.
Complete the TODOs to practice control flow structures.
"""

print("=== Exercise 2: Control Flow ===\n")

# TODO 1: If/else statements
print("1. Conditional Statements:")

# Get a number from user input (simulated here, but you can uncomment for real input)
# number = int(input("Enter a number: "))
number = 15  # Using a fixed value for this exercise

# TODO: Write an if/elif/else statement to check if the number is:
# - Positive (> 0)
# - Negative (< 0) 
# - Zero (== 0)

# Your code here:
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

# TODO 2: Grade calculator
print(f"\n2. Grade Calculator:")
score = 85  # You can change this value

# TODO: Create a grade calculator that assigns letter grades:
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60

# Your code here:


# TODO 3: For loops
print(f"\n3. For Loops:")

# TODO: Print numbers 1 to 10 using a for loop
print("Numbers 1 to 10:")
# Your code here:


# TODO: Print only even numbers from 1 to 20
print("Even numbers from 1 to 20:")
# Your code here:


# TODO 4: While loops
print(f"\n4. While Loops:")

# TODO: Use a while loop to print countdown from 5 to 1
print("Countdown:")
countdown = 5
# Your code here:


# TODO 5: Nested loops - multiplication table
print(f"\n5. Nested Loops - Multiplication Table (1-5):")
# TODO: Create a 5x5 multiplication table using nested loops
# Format: 1 x 1 = 1, 1 x 2 = 2, etc.

# Your code here:


# TODO 6: Loop control - break and continue
print(f"\n6. Loop Control:")

# TODO: Print numbers 1 to 10, but skip 5 and stop at 8
print("Numbers 1 to 10, skip 5, stop at 8:")
for i in range(1, 11):
    # Your code here:
    pass

# TODO 7: Challenge - FizzBuzz
print(f"\n7. Challenge - FizzBuzz:")
# Print numbers 1 to 20, but:
# - Print "Fizz" if divisible by 3
# - Print "Buzz" if divisible by 5  
# - Print "FizzBuzz" if divisible by both 3 and 5

# Your code here:


# TODO 8: List iteration
print(f"\n8. List Iteration:")
fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# TODO: Print each fruit with its index
print("Fruits with index:")
# Your code here:


# TODO: Print only fruits that start with 'a' or 'o'
print("Fruits starting with 'a' or 'o':")
# Your code here:


print(f"\n✅ Exercise 2 complete! Check solutions/02_control_flow_solution.py")

# Self-test questions:
"""
1. What's the difference between 'break' and 'continue'?
2. Can you use 'else' with loops? What happens?
3. How do you create an infinite loop? How do you stop it?
4. What's the difference between 'for' and 'while' loops?
"""