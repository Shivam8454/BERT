#!/usr/bin/env python3
"""
Intermediate Exercise 3: Error Handling and Exceptions

Learn about handling errors gracefully in Python.
Complete the TODOs to practice exception handling techniques.
"""

print("=== Intermediate Exercise 3: Error Handling ===\n")

# TODO 1: Basic exception handling
print("1. Basic Exception Handling:")

def safe_division(a, b):
    """Safely divide two numbers."""
    # TODO: Handle ZeroDivisionError
    # Return the result or an error message
    pass

def safe_list_access(lst, index):
    """Safely access a list element by index."""
    # TODO: Handle IndexError
    # Return the element or None if index is invalid
    pass

def safe_dictionary_access(dictionary, key):
    """Safely access a dictionary value."""
    # TODO: Handle KeyError
    # Return the value or a default message
    pass

def safe_string_to_int(string_value):
    """Safely convert string to integer."""
    # TODO: Handle ValueError
    # Return the integer or None if conversion fails
    pass

# Test basic exception handling
# print(f"Division: {safe_division(10, 2)}")
# print(f"Division by zero: {safe_division(10, 0)}")
# print(f"List access: {safe_list_access([1, 2, 3], 1)}")
# print(f"Invalid index: {safe_list_access([1, 2, 3], 10)}")
# print(f"Dict access: {safe_dictionary_access({'name': 'Alice'}, 'name')}")
# print(f"Missing key: {safe_dictionary_access({'name': 'Alice'}, 'age')}")
# print(f"String to int: {safe_string_to_int('123')}")
# print(f"Invalid string: {safe_string_to_int('abc')}")

# TODO 2: Multiple exception types
print(f"\n2. Multiple Exception Types:")

def process_data(data):
    """Process various types of data with different error handling."""
    try:
        # TODO: Handle multiple exception types
        if isinstance(data, str):
            result = int(data) * 2
        elif isinstance(data, list):
            result = sum(data) / len(data)
        elif isinstance(data, dict):
            result = data['value'] ** 2
        else:
            raise TypeError("Unsupported data type")
        
        return result
    
    except ValueError as e:
        # TODO: Handle ValueError (string conversion)
        pass
    except ZeroDivisionError as e:
        # TODO: Handle ZeroDivisionError (empty list)
        pass
    except KeyError as e:
        # TODO: Handle KeyError (missing dictionary key)
        pass
    except TypeError as e:
        # TODO: Handle TypeError (unsupported type)
        pass
    except Exception as e:
        # TODO: Handle any other unexpected errors
        pass

# Test multiple exception handling
# test_data = ["123", [1, 2, 3, 4], {"value": 5}, [], {"other": 10}, "abc", 42]
# for data in test_data:
#     result = process_data(data)
#     print(f"Processing {data}: {result}")

# TODO 3: Custom exceptions
print(f"\n3. Custom Exceptions:")

class ValidationError(Exception):
    """Custom exception for validation errors."""
    def __init__(self, message, field_name=None):
        # TODO: Initialize custom exception with message and optional field name
        pass

class BankAccountError(Exception):
    """Base exception for bank account operations."""
    pass

class InsufficientFundsError(BankAccountError):
    """Exception for insufficient funds."""
    def __init__(self, attempted_amount, available_balance):
        # TODO: Initialize with attempted amount and available balance
        pass

class InvalidAccountError(BankAccountError):
    """Exception for invalid account operations."""
    pass

def validate_email(email):
    """Validate email format."""
    # TODO: Check if email contains @ and .
    # Raise ValidationError if invalid
    if '@' not in email or '.' not in email:
        # TODO: Raise ValidationError with appropriate message
        pass
    return True

def validate_age(age):
    """Validate age is reasonable."""
    # TODO: Check if age is between 0 and 150
    # Raise ValidationError if invalid
    pass

class BankAccount:
    """Bank account with custom error handling."""
    
    def __init__(self, account_number, initial_balance=0):
        if not account_number:
            raise InvalidAccountError("Account number cannot be empty")
        
        self.account_number = account_number
        self.balance = initial_balance
    
    def withdraw(self, amount):
        """Withdraw money with proper error handling."""
        # TODO: Check if amount is positive
        # TODO: Check if sufficient funds available
        # TODO: Raise appropriate custom exceptions
        pass
    
    def deposit(self, amount):
        """Deposit money with validation."""
        # TODO: Check if amount is positive
        # TODO: Add to balance if valid
        pass

# Test custom exceptions
# try:
#     validate_email("invalid-email")
# except ValidationError as e:
#     print(f"Email validation error: {e}")

# try:
#     validate_age(200)
# except ValidationError as e:
#     print(f"Age validation error: {e}")

# try:
#     account = BankAccount("12345", 100)
#     account.withdraw(150)
# except InsufficientFundsError as e:
#     print(f"Banking error: {e}")

# TODO 4: Exception context and chaining
print(f"\n4. Exception Context and Chaining:")

def read_config_file(filename):
    """Read configuration file with context preservation."""
    try:
        # TODO: Try to open and read file
        with open(filename, 'r') as file:
            config_data = file.read()
            # TODO: Try to parse as JSON
            import json
            config = json.loads(config_data)
            return config
    except FileNotFoundError as e:
        # TODO: Re-raise with context using 'raise ... from e'
        pass
    except json.JSONDecodeError as e:
        # TODO: Re-raise with context
        pass

def process_configuration():
    """Process configuration with exception chaining."""
    try:
        config = read_config_file('nonexistent.json')
        return config
    except Exception as e:
        # TODO: Log the error and re-raise
        print(f"Configuration processing failed: {e}")
        print(f"Original cause: {e.__cause__}")
        raise

# Test exception chaining
# try:
#     process_configuration()
# except Exception as e:
#     print(f"Final error: {e}")

# TODO 5: Using finally and context managers
print(f"\n5. Finally and Context Managers:")

def risky_file_operation(filename):
    """Demonstrate finally block usage."""
    file = None
    try:
        # TODO: Open file and process
        file = open(filename, 'r')
        content = file.read()
        # Simulate some processing that might fail
        result = len(content) / 0  # This will cause ZeroDivisionError
        return result
    except FileNotFoundError:
        # TODO: Handle file not found
        pass
    except ZeroDivisionError:
        # TODO: Handle division error
        pass
    finally:
        # TODO: Ensure file is closed in finally block
        pass

class ManagedResource:
    """Context manager for resource management."""
    
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.is_open = False
    
    def __enter__(self):
        """Enter context manager."""
        # TODO: Setup resource
        print(f"Opening resource: {self.resource_name}")
        self.is_open = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit context manager."""
        # TODO: Cleanup resource
        print(f"Closing resource: {self.resource_name}")
        self.is_open = False
        
        # TODO: Handle exceptions if needed
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
        
        # Return False to propagate exceptions
        return False
    
    def do_work(self):
        """Do some work with the resource."""
        if not self.is_open:
            raise RuntimeError("Resource is not open")
        print(f"Working with {self.resource_name}")

# Test context manager
# with ManagedResource("database_connection") as resource:
#     resource.do_work()

# TODO 6: Error logging and debugging
print(f"\n6. Error Logging and Debugging:")

import logging
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide_with_logging(a, b):
    """Division with comprehensive error logging."""
    try:
        # TODO: Log the operation
        logging.info(f"Attempting to divide {a} by {b}")
        result = a / b
        logging.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError as e:
        # TODO: Log the error with details
        logging.error(f"Division by zero error: {e}")
        logging.debug(f"Inputs were: a={a}, b={b}")
        return None
    except Exception as e:
        # TODO: Log unexpected errors with full traceback
        logging.error(f"Unexpected error in division: {e}")
        logging.error(f"Full traceback: {traceback.format_exc()}")
        return None

def complex_calculation(data_list):
    """Complex calculation with detailed error tracking."""
    try:
        # TODO: Process list with error tracking
        total = 0
        for i, value in enumerate(data_list):
            try:
                # TODO: Convert to float and add
                float_value = float(value)
                total += float_value
                logging.debug(f"Processed item {i}: {value} -> {float_value}")
            except ValueError as e:
                # TODO: Log individual item errors but continue
                logging.warning(f"Skipping invalid item at index {i}: {value} ({e})")
                continue
        
        # TODO: Calculate average
        average = total / len(data_list)
        return average
    
    except ZeroDivisionError:
        logging.error("Cannot calculate average of empty list")
        return None
    except Exception as e:
        logging.error(f"Unexpected error in calculation: {e}")
        return None

# Test error logging
# divide_with_logging(10, 2)
# divide_with_logging(10, 0)
# test_data = ["1", "2.5", "abc", "4", "", "5.5"]
# result = complex_calculation(test_data)
# print(f"Calculation result: {result}")

# TODO 7: Challenge - Robust data processor
print(f"\n7. Challenge - Robust Data Processor:")

class DataProcessor:
    """Robust data processor with comprehensive error handling."""
    
    def __init__(self):
        self.processed_count = 0
        self.error_count = 0
        self.errors = []
    
    def process_item(self, item, index):
        """Process a single data item."""
        try:
            # TODO: Handle different data types
            if isinstance(item, str):
                # Try to convert to number
                if '.' in item:
                    return float(item)
                else:
                    return int(item)
            elif isinstance(item, (int, float)):
                return item
            elif isinstance(item, dict):
                # Extract 'value' key
                return item['value']
            elif isinstance(item, list):
                # Return sum of list
                return sum(item)
            else:
                raise TypeError(f"Unsupported type: {type(item)}")
        
        except (ValueError, TypeError, KeyError) as e:
            # TODO: Log error and store details
            error_info = {
                'index': index,
                'item': item,
                'error_type': type(e).__name__,
                'error_message': str(e)
            }
            self.errors.append(error_info)
            self.error_count += 1
            return None
    
    def process_batch(self, data_list, fail_fast=False):
        """Process a batch of data items."""
        results = []
        
        for i, item in enumerate(data_list):
            try:
                result = self.process_item(item, i)
                if result is not None:
                    results.append(result)
                    self.processed_count += 1
                
            except Exception as e:
                if fail_fast:
                    # TODO: Re-raise immediately
                    raise
                else:
                    # TODO: Continue processing other items
                    continue
        
        return results
    
    def get_statistics(self):
        """Get processing statistics."""
        return {
            'processed_count': self.processed_count,
            'error_count': self.error_count,
            'success_rate': self.processed_count / (self.processed_count + self.error_count) if (self.processed_count + self.error_count) > 0 else 0,
            'errors': self.errors
        }
    
    def reset(self):
        """Reset processor statistics."""
        self.processed_count = 0
        self.error_count = 0
        self.errors = []

# Test robust data processor
# processor = DataProcessor()
# test_data = [
#     "123", "45.6", {"value": 10}, [1, 2, 3], "invalid", 
#     {"other": 5}, [], "78.9", None, 42
# ]
# 
# results = processor.process_batch(test_data)
# stats = processor.get_statistics()
# 
# print(f"Processed results: {results}")
# print(f"Statistics: {stats}")

print(f"\n✅ Intermediate Exercise 3 complete! Check solutions/03_error_handling_solution.py")

# Self-test questions:
"""
1. What's the difference between Exception and BaseException?
2. When should you use specific exception types vs generic Exception?
3. How do you preserve exception context when re-raising?
4. What's the purpose of the finally block?
5. When would you create custom exceptions?
"""