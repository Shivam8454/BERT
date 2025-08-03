#!/usr/bin/env python3
"""
Intermediate Exercise 2: File Handling and I/O

Learn about reading, writing, and manipulating files in Python.
Complete the TODOs to practice file operations.
"""

import os
import json
import csv
from datetime import datetime

print("=== Intermediate Exercise 2: File Handling ===\n")

# TODO 1: Basic file operations
print("1. Basic File Operations:")

def create_sample_file():
    """Create a sample text file for testing."""
    content = """Python is a powerful programming language.
It's great for beginners and experts alike.
Python emphasizes readability and simplicity.
This is a sample file for practicing file operations.
"""
    # TODO: Write this content to a file called 'sample.txt'
    # Use 'with' statement and 'w' mode
    pass

def read_entire_file(filename):
    """Read and return the entire content of a file."""
    # TODO: Open file in read mode and return its content
    # Handle FileNotFoundError
    pass

def read_file_lines(filename):
    """Read and return all lines as a list."""
    # TODO: Read file and return list of lines
    # Strip newline characters from each line
    pass

def count_words_in_file(filename):
    """Count total words in a file."""
    # TODO: Read file and count words
    # Split by whitespace and count
    pass

def append_to_file(filename, text):
    """Append text to a file."""
    # TODO: Open file in append mode and add text
    pass

# Test basic file operations
# create_sample_file()
# print("File content:")
# print(read_entire_file('sample.txt'))
# print(f"Lines: {read_file_lines('sample.txt')}")
# print(f"Word count: {count_words_in_file('sample.txt')}")
# append_to_file('sample.txt', '\nThis line was appended!')

# TODO 2: Working with CSV files
print(f"\n2. CSV File Operations:")

def create_student_csv():
    """Create a CSV file with student data."""
    students = [
        ['Name', 'Age', 'Grade', 'Subject'],
        ['Alice', 20, 85, 'Math'],
        ['Bob', 19, 92, 'Science'],
        ['Charlie', 21, 78, 'English'],
        ['Diana', 20, 96, 'Math']
    ]
    
    # TODO: Write students data to 'students.csv'
    # Use csv.writer
    pass

def read_csv_file(filename):
    """Read CSV file and return data as list of dictionaries."""
    # TODO: Read CSV file and return list of dictionaries
    # Use csv.DictReader
    pass

def add_student_to_csv(filename, student_data):
    """Add a new student to the CSV file."""
    # TODO: Append student data to CSV file
    # student_data is a dictionary with keys: Name, Age, Grade, Subject
    pass

def find_students_by_subject(filename, subject):
    """Find all students studying a specific subject."""
    # TODO: Read CSV and filter by subject
    pass

def calculate_average_grade(filename):
    """Calculate average grade of all students."""
    # TODO: Read CSV and calculate average grade
    pass

# Test CSV operations
# create_student_csv()
# students = read_csv_file('students.csv')
# print("Students:", students)
# add_student_to_csv('students.csv', {'Name': 'Eve', 'Age': 22, 'Grade': 88, 'Subject': 'Science'})
# math_students = find_students_by_subject('students.csv', 'Math')
# print("Math students:", math_students)
# avg_grade = calculate_average_grade('students.csv')
# print(f"Average grade: {avg_grade:.1f}")

# TODO 3: JSON file operations
print(f"\n3. JSON File Operations:")

def create_config_json():
    """Create a configuration JSON file."""
    config = {
        "app_name": "Python Practice App",
        "version": "1.0.0",
        "settings": {
            "debug": True,
            "max_connections": 100,
            "timeout": 30
        },
        "features": ["logging", "caching", "authentication"],
        "created_at": datetime.now().isoformat()
    }
    
    # TODO: Write config to 'config.json'
    # Use json.dump with indent=2
    pass

def read_json_file(filename):
    """Read and return JSON data."""
    # TODO: Read JSON file and return data
    # Handle JSONDecodeError
    pass

def update_json_config(filename, key, value):
    """Update a configuration value in JSON file."""
    # TODO: Read JSON, update key, write back to file
    pass

def add_feature_to_config(filename, feature):
    """Add a new feature to the features list."""
    # TODO: Read JSON, add feature to list, write back
    pass

# Test JSON operations
# create_config_json()
# config = read_json_file('config.json')
# print("Config:", config)
# update_json_config('config.json', 'version', '1.1.0')
# add_feature_to_config('config.json', 'monitoring')

# TODO 4: Directory operations
print(f"\n4. Directory Operations:")

def create_directory_structure():
    """Create a sample directory structure."""
    directories = [
        'test_dir',
        'test_dir/subdirectory',
        'test_dir/another_sub',
        'test_dir/files'
    ]
    
    # TODO: Create all directories
    # Use os.makedirs with exist_ok=True
    pass

def list_directory_contents(path):
    """List all contents of a directory."""
    # TODO: Return list of files and directories in path
    # Handle case where directory doesn't exist
    pass

def find_files_with_extension(directory, extension):
    """Find all files with specific extension in directory."""
    # TODO: Walk through directory and find files with extension
    # Use os.walk or os.listdir
    pass

def get_file_info(filepath):
    """Get information about a file."""
    # TODO: Return dictionary with file info:
    # - size (in bytes)
    # - creation time
    # - modification time
    # - is_file or is_directory
    # Use os.path or pathlib
    pass

def copy_file(source, destination):
    """Copy a file from source to destination."""
    # TODO: Copy file content from source to destination
    # Create destination directory if it doesn't exist
    pass

# Test directory operations
# create_directory_structure()
# contents = list_directory_contents('test_dir')
# print("Directory contents:", contents)
# # Create some test files
# with open('test_dir/test1.txt', 'w') as f:
#     f.write('Test file 1')
# with open('test_dir/test2.py', 'w') as f:
#     f.write('print("Hello")')
# txt_files = find_files_with_extension('test_dir', '.txt')
# print("Text files:", txt_files)

# TODO 5: File processing challenge
print(f"\n5. File Processing Challenge:")

def create_log_file():
    """Create a sample log file."""
    log_entries = [
        "2024-01-01 10:30:15 INFO User logged in: alice",
        "2024-01-01 10:31:22 INFO Page accessed: /dashboard",
        "2024-01-01 10:32:45 WARNING Slow query detected: 2.5s",
        "2024-01-01 10:33:12 ERROR Database connection failed",
        "2024-01-01 10:34:01 INFO User logged out: alice",
        "2024-01-01 10:35:30 INFO User logged in: bob",
        "2024-01-01 10:36:15 ERROR File not found: config.xml",
        "2024-01-01 10:37:22 INFO User logged out: bob"
    ]
    
    # TODO: Write log entries to 'app.log'
    pass

def parse_log_file(filename):
    """Parse log file and extract structured data."""
    # TODO: Parse each line and extract:
    # - timestamp
    # - log level (INFO, WARNING, ERROR)
    # - message
    # Return list of dictionaries
    pass

def filter_logs_by_level(log_data, level):
    """Filter log entries by level."""
    # TODO: Return only logs with specified level
    pass

def count_logs_by_level(log_data):
    """Count logs by level."""
    # TODO: Return dictionary with count for each level
    pass

def find_user_sessions(log_data):
    """Find user login/logout sessions."""
    # TODO: Extract user sessions from login/logout events
    # Return list of dictionaries with user, login_time, logout_time
    pass

# Test log processing
# create_log_file()
# logs = parse_log_file('app.log')
# print("Parsed logs:", logs[:2])  # Show first 2
# error_logs = filter_logs_by_level(logs, 'ERROR')
# print("Error logs:", error_logs)
# log_counts = count_logs_by_level(logs)
# print("Log counts:", log_counts)
# sessions = find_user_sessions(logs)
# print("User sessions:", sessions)

# TODO 6: Challenge - File backup system
print(f"\n6. Challenge - File Backup System:")

class FileBackup:
    """Simple file backup system."""
    
    def __init__(self, backup_dir='backups'):
        self.backup_dir = backup_dir
        # TODO: Create backup directory if it doesn't exist
    
    def backup_file(self, source_file):
        """Create a backup of a file with timestamp."""
        # TODO: Copy file to backup directory with timestamp in name
        # Format: original_name_YYYYMMDD_HHMMSS.extension
        pass
    
    def list_backups(self, original_filename=None):
        """List all backups or backups for specific file."""
        # TODO: List backup files, optionally filter by original filename
        pass
    
    def restore_backup(self, backup_filename, restore_path):
        """Restore a backup to specified path."""
        # TODO: Copy backup file to restore path
        pass
    
    def cleanup_old_backups(self, days_old=30):
        """Remove backups older than specified days."""
        # TODO: Remove backup files older than days_old
        # Use file modification time
        pass

# Test backup system
# backup_system = FileBackup()
# # Create a test file to backup
# with open('important_data.txt', 'w') as f:
#     f.write('This is important data that needs backup.')
# backup_system.backup_file('important_data.txt')
# backups = backup_system.list_backups()
# print("Available backups:", backups)

# TODO 7: Challenge - Text file analyzer
print(f"\n7. Challenge - Text File Analyzer:")

class TextAnalyzer:
    """Analyze text files for various statistics."""
    
    def __init__(self, filename):
        self.filename = filename
        self.content = self._read_file()
    
    def _read_file(self):
        """Read file content."""
        # TODO: Read and return file content
        pass
    
    def word_frequency(self):
        """Return dictionary of word frequencies."""
        # TODO: Count frequency of each word (case-insensitive)
        # Remove punctuation and convert to lowercase
        pass
    
    def character_frequency(self):
        """Return dictionary of character frequencies."""
        # TODO: Count frequency of each character (excluding spaces)
        pass
    
    def sentence_count(self):
        """Count number of sentences."""
        # TODO: Count sentences by counting periods, exclamations, questions
        pass
    
    def average_word_length(self):
        """Calculate average word length."""
        # TODO: Calculate average length of words
        pass
    
    def longest_word(self):
        """Find the longest word."""
        # TODO: Return the longest word in the text
        pass
    
    def readability_score(self):
        """Calculate simple readability score."""
        # TODO: Use average sentence length and average word length
        # Simple formula: score = avg_sentence_length + avg_word_length
        pass
    
    def generate_report(self):
        """Generate comprehensive analysis report."""
        # TODO: Create a report with all statistics
        pass

# Test text analyzer
# create_sample_file()  # Make sure we have a file to analyze
# analyzer = TextAnalyzer('sample.txt')
# print("Analysis Report:")
# print(analyzer.generate_report())

print(f"\n✅ Intermediate Exercise 2 complete! Check solutions/02_file_handling_solution.py")

# Self-test questions:
"""
1. What's the difference between 'r', 'w', 'a', and 'x' file modes?
2. Why should you use 'with' statement when working with files?
3. How do you handle different text encodings when reading files?
4. What's the difference between csv.reader and csv.DictReader?
5. When would you use JSON vs CSV for data storage?
"""