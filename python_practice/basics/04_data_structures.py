#!/usr/bin/env python3
"""
Exercise 4: Data Structures (Lists, Dictionaries, Tuples, Sets)

Learn about Python's built-in data structures and their operations.
Complete the TODOs to practice working with different data types.
"""

print("=== Exercise 4: Data Structures ===\n")

# TODO 1: Lists - Creation and basic operations
print("1. Lists:")

# TODO: Create a list of your favorite colors
favorite_colors = []  # Replace with your colors

# TODO: Add a new color to the end of the list
# Use the append() method

# TODO: Insert a color at the beginning of the list
# Use the insert() method

# TODO: Remove a specific color from the list
# Use the remove() method

print(f"Favorite colors: {favorite_colors}")
print(f"First color: {favorite_colors[0] if favorite_colors else 'None'}")
print(f"Last color: {favorite_colors[-1] if favorite_colors else 'None'}")
print(f"Number of colors: {len(favorite_colors)}")

# TODO 2: List slicing and comprehensions
print(f"\n2. List Operations:")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: Get the first 5 numbers using slicing
first_five = None  # Your code here

# TODO: Get every other number using slicing
every_other = None  # Your code here

# TODO: Create a list of squares using list comprehension
squares = []  # Your code here: [x**2 for x in numbers]

# TODO: Create a list of even numbers using list comprehension
evens = []  # Your code here

print(f"Original numbers: {numbers}")
print(f"First five: {first_five}")
print(f"Every other: {every_other}")
print(f"Squares: {squares}")
print(f"Even numbers: {evens}")

# TODO 3: Dictionaries - Key-value pairs
print(f"\n3. Dictionaries:")

# TODO: Create a dictionary representing a person
person = {
    # Add keys: name, age, city, occupation
}

# TODO: Add a new key-value pair to the dictionary
# Add 'email' key

# TODO: Update an existing value
# Change the age

# TODO: Remove a key from the dictionary
# Remove 'city' using pop() or del

print(f"Person info: {person}")
print(f"Name: {person.get('name', 'Not found')}")
print(f"All keys: {list(person.keys())}")
print(f"All values: {list(person.values())}")

# TODO 4: Dictionary methods and iteration
print(f"\n4. Dictionary Operations:")

grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}

# TODO: Find the student with the highest grade
best_student = None
highest_grade = 0
# Your code here

# TODO: Create a new dictionary with students who scored above 80
high_scorers = {}  # Your code here

# TODO: Calculate the average grade
total_grade = 0
count = 0
# Your code here
average_grade = 0  # Calculate this

print(f"Grades: {grades}")
print(f"Best student: {best_student} with {highest_grade}")
print(f"High scorers: {high_scorers}")
print(f"Average grade: {average_grade:.1f}")

# TODO 5: Tuples - Immutable sequences
print(f"\n5. Tuples:")

# TODO: Create a tuple representing coordinates (x, y, z)
coordinates = ()  # Your code here

# TODO: Unpack the tuple into separate variables
x, y, z = 0, 0, 0  # Your code here

# TODO: Create a tuple of tuples representing points
points = (
    # Add at least 3 coordinate tuples
)

print(f"Coordinates: {coordinates}")
print(f"X: {x}, Y: {y}, Z: {z}")
print(f"Points: {points}")
print(f"First point: {points[0] if points else 'None'}")

# TODO 6: Sets - Unique collections
print(f"\n6. Sets:")

# TODO: Create sets and perform set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# TODO: Find the union (all unique elements)
union_set = set()  # Your code here

# TODO: Find the intersection (common elements)
intersection_set = set()  # Your code here

# TODO: Find the difference (elements in set1 but not set2)
difference_set = set()  # Your code here

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")

# TODO 7: Nested data structures
print(f"\n7. Nested Data Structures:")

# TODO: Create a list of dictionaries representing students
students = [
    # Add at least 3 student dictionaries with name, age, and grades
]

# TODO: Calculate the average grade for each student
for student in students:
    # Your code here to calculate and add 'average_grade' to each student
    pass

# TODO: Find the student with the highest average
best_student_overall = None  # Your code here

print(f"Students: {students}")
print(f"Best overall student: {best_student_overall}")

# TODO 8: Challenge - Data structure conversion
print(f"\n8. Challenge - Data Conversions:")

# Start with this string of numbers
number_string = "1,2,3,2,4,3,5,4,6"

# TODO: Convert to list of integers
number_list = []  # Your code here

# TODO: Convert to set (removes duplicates)
number_set = set()  # Your code here

# TODO: Convert back to sorted list
sorted_unique = []  # Your code here

# TODO: Create a frequency dictionary
frequency = {}  # Your code here: count how many times each number appears

print(f"Original string: {number_string}")
print(f"Number list: {number_list}")
print(f"Unique numbers: {number_set}")
print(f"Sorted unique: {sorted_unique}")
print(f"Frequency: {frequency}")

print(f"\n✅ Exercise 4 complete! Check solutions/04_data_structures_solution.py")

# Self-test questions:
"""
1. What's the difference between a list and a tuple?
2. When would you use a set instead of a list?
3. How do you check if a key exists in a dictionary?
4. Can you have a list as a dictionary value? A dictionary as a list element?
5. What happens when you try to add a duplicate element to a set?
"""