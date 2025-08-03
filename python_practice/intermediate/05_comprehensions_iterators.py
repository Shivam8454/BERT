#!/usr/bin/env python3
"""
Intermediate Exercise 5: Comprehensions and Iterators

Learn about list/dict/set comprehensions, generator expressions, and iterators.
Complete the TODOs to practice advanced iteration techniques.
"""

print("=== Intermediate Exercise 5: Comprehensions and Iterators ===\n")

# TODO 1: List comprehensions
print("1. List Comprehensions:")

def basic_list_comprehensions():
    """Practice basic list comprehensions."""
    # Sample data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ["hello", "world", "python", "programming", "code"]
    
    # TODO: Create list of squares using comprehension
    squares = []  # [x**2 for x in numbers]
    
    # TODO: Create list of even numbers using comprehension
    evens = []  # [x for x in numbers if x % 2 == 0]
    
    # TODO: Create list of word lengths using comprehension
    lengths = []  # [len(word) for word in words]
    
    # TODO: Create list of uppercase words longer than 4 characters
    long_upper = []  # [word.upper() for word in words if len(word) > 4]
    
    # TODO: Create list of tuples (number, square) for odd numbers
    odd_squares = []  # [(x, x**2) for x in numbers if x % 2 == 1]
    
    print(f"Original numbers: {numbers}")
    print(f"Squares: {squares}")
    print(f"Even numbers: {evens}")
    print(f"Word lengths: {lengths}")
    print(f"Long uppercase words: {long_upper}")
    print(f"Odd number squares: {odd_squares}")

# Test basic comprehensions
# basic_list_comprehensions()

# TODO 2: Nested list comprehensions
print(f"\n2. Nested List Comprehensions:")

def nested_comprehensions():
    """Practice nested list comprehensions."""
    # Create a 3x3 matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # TODO: Flatten the matrix using nested comprehension
    flattened = []  # [item for row in matrix for item in row]
    
    # TODO: Create list of all even numbers from the matrix
    matrix_evens = []  # [item for row in matrix for item in row if item % 2 == 0]
    
    # TODO: Transpose the matrix using nested comprehension
    transposed = []  # [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    # TODO: Create multiplication table using nested comprehension
    mult_table = []  # [[i * j for j in range(1, 6)] for i in range(1, 6)]
    
    print(f"Original matrix: {matrix}")
    print(f"Flattened: {flattened}")
    print(f"Even numbers: {matrix_evens}")
    print(f"Transposed: {transposed}")
    print(f"Multiplication table: {mult_table}")

# Test nested comprehensions
# nested_comprehensions()

# TODO 3: Dictionary comprehensions
print(f"\n3. Dictionary Comprehensions:")

def dictionary_comprehensions():
    """Practice dictionary comprehensions."""
    # Sample data
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # TODO: Create dict mapping words to their lengths
    word_lengths = {}  # {word: len(word) for word in words}
    
    # TODO: Create dict mapping numbers to their squares
    squares_dict = {}  # {x: x**2 for x in numbers}
    
    # TODO: Create dict of even numbers and their cubes
    even_cubes = {}  # {x: x**3 for x in numbers if x % 2 == 0}
    
    # TODO: Create dict mapping first letter to list of words starting with it
    letter_groups = {}  # Use defaultdict or dict.get()
    
    # TODO: Invert a dictionary (swap keys and values)
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    inverted = {}  # {v: k for k, v in original_dict.items()}
    
    print(f"Word lengths: {word_lengths}")
    print(f"Number squares: {squares_dict}")
    print(f"Even cubes: {even_cubes}")
    print(f"Letter groups: {letter_groups}")
    print(f"Original dict: {original_dict}")
    print(f"Inverted dict: {inverted}")

# Test dictionary comprehensions
# dictionary_comprehensions()

# TODO 4: Set comprehensions
print(f"\n4. Set Comprehensions:")

def set_comprehensions():
    """Practice set comprehensions."""
    # Sample data
    sentence = "the quick brown fox jumps over the lazy dog"
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    
    # TODO: Create set of unique characters in sentence
    unique_chars = set()  # {char for char in sentence if char.isalpha()}
    
    # TODO: Create set of unique word lengths
    word_lengths = set()  # {len(word) for word in sentence.split()}
    
    # TODO: Create set of unique numbers (remove duplicates)
    unique_numbers = set()  # {x for x in numbers}
    
    # TODO: Create set of vowels found in the sentence
    vowels = "aeiou"
    found_vowels = set()  # {char for char in sentence.lower() if char in vowels}
    
    # TODO: Create set of squared even numbers
    even_squares = set()  # {x**2 for x in range(1, 11) if x % 2 == 0}
    
    print(f"Sentence: {sentence}")
    print(f"Unique characters: {unique_chars}")
    print(f"Word lengths: {word_lengths}")
    print(f"Unique numbers: {unique_numbers}")
    print(f"Found vowels: {found_vowels}")
    print(f"Even squares: {even_squares}")

# Test set comprehensions
# set_comprehensions()

# TODO 5: Generator expressions
print(f"\n5. Generator Expressions:")

def generator_expressions():
    """Practice generator expressions."""
    # TODO: Create generator for squares of numbers 1-10
    squares_gen = None  # (x**2 for x in range(1, 11))
    
    # TODO: Create generator for even numbers from 1-20
    evens_gen = None  # (x for x in range(1, 21) if x % 2 == 0)
    
    # TODO: Use generator to read file lines (simulated)
    lines = ["line 1", "line 2", "line 3", "line 4", "line 5"]
    long_lines_gen = None  # (line for line in lines if len(line) > 6)
    
    # TODO: Create generator for Fibonacci numbers
    def fibonacci_gen(n):
        """Generator for Fibonacci sequence."""
        # TODO: Implement Fibonacci generator
        pass
    
    # TODO: Memory-efficient processing of large data
    def process_large_data():
        """Demonstrate memory efficiency of generators."""
        # TODO: Compare list comprehension vs generator expression memory usage
        import sys
        
        # List comprehension (loads all in memory)
        list_comp = [x**2 for x in range(10000)]
        list_size = sys.getsizeof(list_comp)
        
        # Generator expression (lazy evaluation)
        gen_exp = (x**2 for x in range(10000))
        gen_size = sys.getsizeof(gen_exp)
        
        print(f"List comprehension size: {list_size} bytes")
        print(f"Generator expression size: {gen_size} bytes")
        print(f"Memory savings: {list_size - gen_size} bytes")
        
        return list_comp, gen_exp
    
    # Test generators
    print("First 5 squares:", list(x for x, _ in zip(squares_gen, range(5))))
    print("Even numbers:", list(evens_gen))
    print("Long lines:", list(long_lines_gen))
    
    # Test Fibonacci generator
    fib_gen = fibonacci_gen(10)
    print("Fibonacci sequence:", list(fib_gen))
    
    # Test memory efficiency
    process_large_data()

# Test generator expressions
# generator_expressions()

# TODO 6: Custom iterators
print(f"\n6. Custom Iterators:")

class CountDown:
    """Custom iterator that counts down from a number."""
    
    def __init__(self, start):
        # TODO: Initialize the countdown
        pass
    
    def __iter__(self):
        # TODO: Return iterator object (self)
        pass
    
    def __next__(self):
        # TODO: Return next value or raise StopIteration
        pass

class FibonacciIterator:
    """Custom iterator for Fibonacci sequence."""
    
    def __init__(self, max_count):
        # TODO: Initialize Fibonacci iterator
        pass
    
    def __iter__(self):
        # TODO: Return iterator object
        pass
    
    def __next__(self):
        # TODO: Generate next Fibonacci number
        pass

class SquareRange:
    """Custom iterator that yields squares of numbers in a range."""
    
    def __init__(self, start, end):
        # TODO: Initialize square range iterator
        pass
    
    def __iter__(self):
        # TODO: Return iterator object
        pass
    
    def __next__(self):
        # TODO: Generate next square
        pass

# Test custom iterators
def test_custom_iterators():
    """Test the custom iterator classes."""
    # TODO: Test CountDown iterator
    print("Countdown from 5:")
    # for num in CountDown(5):
    #     print(num)
    
    # TODO: Test Fibonacci iterator
    print("First 8 Fibonacci numbers:")
    # for fib in FibonacciIterator(8):
    #     print(fib, end=" ")
    # print()
    
    # TODO: Test SquareRange iterator
    print("Squares from 1 to 5:")
    # for square in SquareRange(1, 6):
    #     print(square, end=" ")
    # print()

# test_custom_iterators()

# TODO 7: itertools module
print(f"\n7. Itertools Module:")

def itertools_examples():
    """Demonstrate useful itertools functions."""
    import itertools
    
    # Sample data
    numbers = [1, 2, 3, 4, 5]
    letters = ['a', 'b', 'c']
    
    # TODO: Use itertools.chain to combine iterables
    combined = None  # list(itertools.chain(numbers, letters))
    
    # TODO: Use itertools.cycle to repeat sequence
    cycled = None  # Take first 10 from itertools.cycle(['A', 'B', 'C'])
    
    # TODO: Use itertools.repeat to repeat single value
    repeated = None  # list(itertools.repeat('hello', 3))
    
    # TODO: Use itertools.count for infinite counting
    counted = None  # Take first 5 from itertools.count(10, 2)
    
    # TODO: Use itertools.combinations for combinations
    combinations = None  # list(itertools.combinations(numbers[:4], 2))
    
    # TODO: Use itertools.permutations for permutations
    permutations = None  # list(itertools.permutations(letters, 2))
    
    # TODO: Use itertools.product for cartesian product
    product = None  # list(itertools.product(numbers[:3], letters[:2]))
    
    # TODO: Use itertools.groupby to group consecutive elements
    data = [1, 1, 2, 2, 2, 3, 1, 1]
    grouped = None  # [(k, list(g)) for k, g in itertools.groupby(data)]
    
    print(f"Combined: {combined}")
    print(f"Cycled: {cycled}")
    print(f"Repeated: {repeated}")
    print(f"Counted: {counted}")
    print(f"Combinations: {combinations}")
    print(f"Permutations: {permutations}")
    print(f"Product: {product}")
    print(f"Grouped: {grouped}")

# Test itertools
# itertools_examples()

# TODO 8: Challenge - Data processing pipeline
print(f"\n8. Challenge - Data Processing Pipeline:")

class DataPipeline:
    """Data processing pipeline using generators and comprehensions."""
    
    def __init__(self, data):
        self.data = data
    
    def filter_data(self, condition):
        """Filter data based on condition function."""
        # TODO: Use generator expression to filter data
        pass
    
    def transform_data(self, transform_func):
        """Transform data using transform function."""
        # TODO: Use generator expression to transform data
        pass
    
    def batch_data(self, batch_size):
        """Batch data into chunks of specified size."""
        # TODO: Create generator that yields batches
        pass
    
    def aggregate_data(self, agg_func):
        """Aggregate data using aggregation function."""
        # TODO: Apply aggregation function to data
        pass
    
    def process(self):
        """Process the entire pipeline and return results."""
        # TODO: Chain all operations and return final result
        pass

def create_sample_data():
    """Create sample data for testing pipeline."""
    import random
    
    # TODO: Create list of dictionaries representing sales data
    data = []
    products = ['laptop', 'phone', 'tablet', 'monitor', 'keyboard']
    regions = ['north', 'south', 'east', 'west']
    
    for i in range(100):
        record = {
            'id': i + 1,
            'product': random.choice(products),
            'region': random.choice(regions),
            'sales': random.randint(100, 1000),
            'quantity': random.randint(1, 10)
        }
        data.append(record)
    
    return data

def pipeline_example():
    """Demonstrate data pipeline usage."""
    # TODO: Create sample data
    data = create_sample_data()
    
    # TODO: Create processing pipeline
    pipeline = DataPipeline(data)
    
    # TODO: Filter for high-value sales (> 500)
    high_value = pipeline.filter_data(lambda x: x['sales'] > 500)
    
    # TODO: Transform to include total value (sales * quantity)
    with_total = pipeline.transform_data(
        lambda x: {**x, 'total_value': x['sales'] * x['quantity']}
    )
    
    # TODO: Group by region and calculate totals
    # This would require more complex aggregation logic
    
    print("Sample processing pipeline created")
    print(f"Total records: {len(data)}")

# Test data pipeline
# pipeline_example()

# TODO 9: Challenge - Custom collection with comprehension support
print(f"\n9. Challenge - Custom Collection:")

class Matrix:
    """Custom matrix class with comprehension support."""
    
    def __init__(self, rows, cols, fill_value=0):
        # TODO: Initialize matrix with given dimensions
        pass
    
    def __getitem__(self, key):
        """Support matrix[row][col] access."""
        # TODO: Implement item access
        pass
    
    def __setitem__(self, key, value):
        """Support matrix[row][col] = value assignment."""
        # TODO: Implement item assignment
        pass
    
    def __iter__(self):
        """Support iteration over matrix rows."""
        # TODO: Implement iteration
        pass
    
    def flatten(self):
        """Return flattened matrix as generator."""
        # TODO: Create generator that yields all elements
        pass
    
    def apply(self, func):
        """Apply function to all elements using comprehension."""
        # TODO: Apply function to create new matrix
        pass
    
    def filter_elements(self, condition):
        """Filter elements that meet condition."""
        # TODO: Return list of elements meeting condition
        pass
    
    def transpose(self):
        """Return transposed matrix."""
        # TODO: Create transposed matrix using comprehension
        pass
    
    def __str__(self):
        """String representation of matrix."""
        # TODO: Format matrix for display
        pass

def test_matrix():
    """Test the custom Matrix class."""
    # TODO: Create 3x3 matrix
    matrix = Matrix(3, 3, 0)
    
    # TODO: Fill with values using comprehension
    # for i in range(3):
    #     for j in range(3):
    #         matrix[i][j] = i * 3 + j + 1
    
    # TODO: Test various operations
    # print("Original matrix:")
    # print(matrix)
    
    # print("Flattened:", list(matrix.flatten()))
    # print("Doubled:", matrix.apply(lambda x: x * 2))
    # print("Even numbers:", matrix.filter_elements(lambda x: x % 2 == 0))
    # print("Transposed:", matrix.transpose())

# test_matrix()

print(f"\n✅ Intermediate Exercise 5 complete! Check solutions/05_comprehensions_iterators_solution.py")

# Self-test questions:
"""
1. What's the difference between a list comprehension and a generator expression?
2. When should you use a generator instead of a list?
3. How do you implement a custom iterator class?
4. What are the benefits of using itertools functions?
5. How can comprehensions improve code readability and performance?
"""