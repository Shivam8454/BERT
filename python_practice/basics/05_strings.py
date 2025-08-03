#!/usr/bin/env python3
"""
Exercise 5: String Manipulation

Learn about working with strings in Python - formatting, methods, and operations.
Complete the TODOs to practice string manipulation techniques.
"""

print("=== Exercise 5: String Manipulation ===\n")

# TODO 1: Basic string operations
print("1. Basic String Operations:")

# Sample text to work with
text = "  Hello, Python World!  "

# TODO: Remove whitespace from both ends
cleaned_text = None  # Use strip() method

# TODO: Convert to uppercase and lowercase
upper_text = None  # Use upper() method
lower_text = None  # Use lower() method

# TODO: Check if text contains certain words
contains_python = None  # Check if "Python" is in text
starts_with_hello = None  # Check if text starts with "Hello"
ends_with_world = None  # Check if text ends with "World!"

print(f"Original: '{text}'")
print(f"Cleaned: '{cleaned_text}'")
print(f"Uppercase: '{upper_text}'")
print(f"Lowercase: '{lower_text}'")
print(f"Contains 'Python': {contains_python}")
print(f"Starts with 'Hello': {starts_with_hello}")
print(f"Ends with 'World!': {ends_with_world}")

# TODO 2: String slicing and indexing
print(f"\n2. String Slicing:")

message = "Python Programming"

# TODO: Extract substrings using slicing
first_word = None      # Get "Python"
second_word = None     # Get "Programming"
first_three = None     # Get first 3 characters
last_three = None      # Get last 3 characters
every_other = None     # Get every other character

print(f"Original: '{message}'")
print(f"First word: '{first_word}'")
print(f"Second word: '{second_word}'")
print(f"First three: '{first_three}'")
print(f"Last three: '{last_three}'")
print(f"Every other: '{every_other}'")

# TODO 3: String methods and manipulation
print(f"\n3. String Methods:")

sentence = "python is awesome and python is fun"

# TODO: Replace words
new_sentence = None  # Replace "python" with "Python"

# TODO: Split the sentence into words
words = []  # Split by spaces

# TODO: Count occurrences
python_count = 0  # Count how many times "python" appears

# TODO: Find the position of a word
awesome_position = -1  # Find position of "awesome"

# TODO: Join words back together
rejoined = ""  # Join words with " - " separator

print(f"Original: '{sentence}'")
print(f"After replacement: '{new_sentence}'")
print(f"Words: {words}")
print(f"'python' appears {python_count} times")
print(f"'awesome' is at position: {awesome_position}")
print(f"Rejoined: '{rejoined}'")

# TODO 4: String formatting
print(f"\n4. String Formatting:")

name = "Alice"
age = 25
height = 1.68
grade = 85.5

# TODO: Use different formatting methods

# Old-style formatting (%)
old_format = ""  # "Name: Alice, Age: 25"

# str.format() method
format_method = ""  # "Alice is 25 years old and 1.68m tall"

# f-string formatting (modern way)
f_string = ""  # "Alice scored 85.5% on the test"

# Formatting numbers
formatted_grade = ""  # Format grade to 1 decimal place

print(f"Old style: {old_format}")
print(f"Format method: {format_method}")
print(f"F-string: {f_string}")
print(f"Formatted grade: {formatted_grade}")

# TODO 5: String validation
print(f"\n5. String Validation:")

test_strings = ["123", "abc", "ABC", "123abc", "  ", ""]

for test_str in test_strings:
    # TODO: Test various string properties
    is_digit = False      # Check if all characters are digits
    is_alpha = False      # Check if all characters are letters
    is_alnum = False      # Check if all characters are alphanumeric
    is_upper = False      # Check if all letters are uppercase
    is_lower = False      # Check if all letters are lowercase
    is_space = False      # Check if string contains only whitespace
    
    print(f"'{test_str}': digit={is_digit}, alpha={is_alpha}, alnum={is_alnum}, "
          f"upper={is_upper}, lower={is_lower}, space={is_space}")

# TODO 6: Text processing challenge
print(f"\n6. Text Processing Challenge:")

text_to_process = """
Python is a high-level, interpreted programming language.
It was created by Guido van Rossum and first released in 1991.
Python emphasizes code readability and simplicity.
"""

# TODO: Clean and analyze the text
cleaned_text = ""  # Remove extra whitespace and newlines
word_count = 0     # Count total words
sentence_count = 0 # Count sentences (by periods)
char_count = 0     # Count characters (excluding spaces)

# TODO: Find the longest word
longest_word = ""

# TODO: Create a word frequency dictionary
word_frequency = {}

print(f"Original text length: {len(text_to_process)} characters")
print(f"Cleaned text: '{cleaned_text[:50]}...'")
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}")
print(f"Character count (no spaces): {char_count}")
print(f"Longest word: '{longest_word}'")
print(f"Most common words: {dict(list(word_frequency.items())[:3])}")

# TODO 7: String encoding and special characters
print(f"\n7. Special Characters and Encoding:")

# TODO: Work with escape characters
quote_text = ""  # String containing: He said, "Hello, World!"
path_text = ""   # String representing a file path: C:\Users\Name\file.txt
multiline = ""   # Multiline string using triple quotes

print(f"Quote: {quote_text}")
print(f"Path: {path_text}")
print(f"Multiline:\n{multiline}")

# TODO 8: Challenge - Text manipulation functions
print(f"\n8. Challenge - Custom Text Functions:")

def reverse_words(text):
    """Reverse the order of words in a sentence."""
    # TODO: Implement this function
    pass

def title_case(text):
    """Convert text to title case (first letter of each word capitalized)."""
    # TODO: Implement this function
    pass

def count_vowels(text):
    """Count the number of vowels in the text."""
    # TODO: Implement this function
    pass

def is_palindrome(text):
    """Check if text reads the same forwards and backwards (ignore case and spaces)."""
    # TODO: Implement this function
    pass

# Test the functions
test_sentence = "hello world python"
palindrome_test = "A man a plan a canal Panama"

print(f"Original: '{test_sentence}'")
print(f"Reversed words: '{reverse_words(test_sentence)}'")
print(f"Title case: '{title_case(test_sentence)}'")
print(f"Vowel count: {count_vowels(test_sentence)}")
print(f"Is palindrome ('{palindrome_test}'): {is_palindrome(palindrome_test)}")

print(f"\n✅ Exercise 5 complete! Check solutions/05_strings_solution.py")

# Self-test questions:
"""
1. What's the difference between single, double, and triple quotes?
2. How do you include a quote character inside a string?
3. What's the difference between split() and partition()?
4. When would you use f-strings vs format() vs % formatting?
5. How do you handle case-insensitive string comparisons?
"""