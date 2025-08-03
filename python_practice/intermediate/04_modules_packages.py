#!/usr/bin/env python3
"""
Intermediate Exercise 4: Modules and Packages

Learn about organizing code into modules and packages.
Complete the TODOs to practice module creation and importing.
"""

import sys
import os
from pathlib import Path

print("=== Intermediate Exercise 4: Modules and Packages ===\n")

# TODO 1: Understanding imports
print("1. Understanding Imports:")

# TODO: Import specific functions from math module
# Import: sqrt, pi, sin, cos

# TODO: Import datetime with an alias
# Import datetime as dt

# TODO: Import all functions from random module (generally not recommended)
# from random import *

# TODO: Import json module
import json

def demonstrate_imports():
    """Demonstrate different import styles."""
    # TODO: Use imported functions
    # Calculate square root of 16
    # Get current date and time
    # Generate random number between 1 and 10
    # Create a JSON string from a dictionary
    pass

# Test imports
# demonstrate_imports()

# TODO 2: Creating your own module
print(f"\n2. Creating Custom Modules:")

# Create a utilities module
def create_utils_module():
    """Create a utilities module file."""
    utils_content = '''"""
Utilities module for common functions.
"""

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Module-level variables
PI = 3.14159
AUTHOR = "Python Practice"
VERSION = "1.0.0"

if __name__ == "__main__":
    # Code that runs when module is executed directly
    print("Utils module - running tests")
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"5! = {factorial(5)}")
'''
    
    # TODO: Write the utils module to a file
    with open('utils.py', 'w') as f:
        f.write(utils_content)
    print("Created utils.py module")

def test_custom_module():
    """Test our custom module."""
    # TODO: Import and use functions from utils module
    # Note: You'll need to run create_utils_module() first
    try:
        import utils
        
        # TODO: Use functions from utils module
        fib_sequence = utils.fibonacci(8)
        is_17_prime = utils.is_prime(17)
        fact_5 = utils.factorial(5)
        
        print(f"Fibonacci(8): {fib_sequence}")
        print(f"Is 17 prime? {is_17_prime}")
        print(f"5! = {fact_5}")
        print(f"Module info: {utils.AUTHOR} v{utils.VERSION}")
        
    except ImportError as e:
        print(f"Could not import utils module: {e}")

# TODO: Create and test custom module
# create_utils_module()
# test_custom_module()

# TODO 3: Package creation
print(f"\n3. Creating Packages:")

def create_math_package():
    """Create a math package with submodules."""
    # Create package directory
    package_dir = Path("mathtools")
    package_dir.mkdir(exist_ok=True)
    
    # Create __init__.py
    init_content = '''"""
MathTools package for mathematical operations.
"""

# Import functions to make them available at package level
from .basic_ops import add, subtract, multiply, divide
from .advanced_ops import power, logarithm, trigonometry
from .statistics import mean, median, mode, standard_deviation

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Practice"

# What gets imported with "from mathtools import *"
__all__ = [
    'add', 'subtract', 'multiply', 'divide',
    'power', 'logarithm', 'trigonometry',
    'mean', 'median', 'mode', 'standard_deviation'
]
'''
    
    # Create basic_ops.py
    basic_ops_content = '''"""
Basic mathematical operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
'''
    
    # Create advanced_ops.py
    advanced_ops_content = '''"""
Advanced mathematical operations.
"""

import math

def power(base, exponent):
    """Calculate base raised to exponent."""
    return base ** exponent

def logarithm(value, base=math.e):
    """Calculate logarithm of value with given base."""
    if value <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    if base == math.e:
        return math.log(value)
    return math.log(value) / math.log(base)

def trigonometry(angle, func='sin'):
    """Calculate trigonometric functions."""
    angle_rad = math.radians(angle)
    if func == 'sin':
        return math.sin(angle_rad)
    elif func == 'cos':
        return math.cos(angle_rad)
    elif func == 'tan':
        return math.tan(angle_rad)
    else:
        raise ValueError("Unsupported trigonometric function")
'''
    
    # Create statistics.py
    statistics_content = '''"""
Statistical operations.
"""

import math
from collections import Counter

def mean(data):
    """Calculate arithmetic mean."""
    if not data:
        raise ValueError("Cannot calculate mean of empty data")
    return sum(data) / len(data)

def median(data):
    """Calculate median."""
    if not data:
        raise ValueError("Cannot calculate median of empty data")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    return sorted_data[n//2]

def mode(data):
    """Find mode(s) of the data."""
    if not data:
        raise ValueError("Cannot calculate mode of empty data")
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [k for k, v in counter.items() if v == max_count]
    return modes[0] if len(modes) == 1 else modes

def standard_deviation(data):
    """Calculate standard deviation."""
    if len(data) < 2:
        raise ValueError("Need at least 2 data points")
    data_mean = mean(data)
    variance = sum((x - data_mean) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)
'''
    
    # TODO: Write all package files
    with open(package_dir / "__init__.py", 'w') as f:
        f.write(init_content)
    
    with open(package_dir / "basic_ops.py", 'w') as f:
        f.write(basic_ops_content)
    
    with open(package_dir / "advanced_ops.py", 'w') as f:
        f.write(advanced_ops_content)
    
    with open(package_dir / "statistics.py", 'w') as f:
        f.write(statistics_content)
    
    print("Created mathtools package")

def test_math_package():
    """Test the math package."""
    try:
        # TODO: Import and test package functions
        import mathtools
        from mathtools import mean, add, power
        from mathtools.trigonometry import trigonometry
        
        # Test basic operations
        print(f"Add: {add(5, 3)}")
        print(f"Power: {power(2, 3)}")
        
        # Test statistics
        data = [1, 2, 3, 4, 5]
        print(f"Mean of {data}: {mean(data)}")
        
        # Test trigonometry
        print(f"Sin(30°): {trigonometry(30, 'sin'):.3f}")
        
    except ImportError as e:
        print(f"Could not import mathtools package: {e}")

# TODO: Create and test package
# create_math_package()
# test_math_package()

# TODO 4: Module search path and sys.path
print(f"\n4. Module Search Path:")

def explore_module_path():
    """Explore Python's module search path."""
    print("Python module search path:")
    for i, path in enumerate(sys.path):
        print(f"{i}: {path}")
    
    # TODO: Add a custom path to sys.path
    custom_path = "/tmp/custom_modules"
    if custom_path not in sys.path:
        sys.path.append(custom_path)
        print(f"\nAdded custom path: {custom_path}")

def find_module_location(module_name):
    """Find where a module is located."""
    try:
        module = __import__(module_name)
        if hasattr(module, '__file__'):
            print(f"{module_name} is located at: {module.__file__}")
        else:
            print(f"{module_name} is a built-in module")
    except ImportError:
        print(f"Module {module_name} not found")

# Test module exploration
# explore_module_path()
# find_module_location('os')
# find_module_location('json')
# find_module_location('sys')

# TODO 5: Relative vs absolute imports
print(f"\n5. Import Styles:")

def create_project_structure():
    """Create a sample project structure."""
    # Create directory structure
    project_dir = Path("myproject")
    project_dir.mkdir(exist_ok=True)
    
    # Create subdirectories
    (project_dir / "core").mkdir(exist_ok=True)
    (project_dir / "utils").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    
    # Create __init__.py files
    for subdir in ["core", "utils", "tests"]:
        (project_dir / subdir / "__init__.py").touch()
    
    # Create main __init__.py
    (project_dir / "__init__.py").touch()
    
    # Create core/database.py
    db_content = '''"""
Database connection module.
"""

class Database:
    def __init__(self, host="localhost"):
        self.host = host
        self.connected = False
    
    def connect(self):
        self.connected = True
        return f"Connected to {self.host}"
    
    def disconnect(self):
        self.connected = False
        return "Disconnected"
'''
    
    # Create utils/helpers.py
    helpers_content = '''"""
Helper utilities.
"""

def format_string(text):
    """Format string to title case."""
    return text.title()

def validate_email(email):
    """Simple email validation."""
    return "@" in email and "." in email
'''
    
    # Create core/models.py
    models_content = '''"""
Data models.
"""

# Absolute import
from myproject.core.database import Database

# Relative import example (when run as part of package)
from .database import Database as DB
from ..utils.helpers import format_string

class User:
    def __init__(self, name, email):
        self.name = format_string(name)
        self.email = email
        self.db = Database()
    
    def save(self):
        self.db.connect()
        result = f"Saved user: {self.name}"
        self.db.disconnect()
        return result
'''
    
    # TODO: Write all files
    with open(project_dir / "core" / "database.py", 'w') as f:
        f.write(db_content)
    
    with open(project_dir / "utils" / "helpers.py", 'w') as f:
        f.write(helpers_content)
    
    with open(project_dir / "core" / "models.py", 'w') as f:
        f.write(models_content)
    
    print("Created project structure")

# TODO: Create project structure
# create_project_structure()

# TODO 6: Dynamic imports and importlib
print(f"\n6. Dynamic Imports:")

def dynamic_import_demo():
    """Demonstrate dynamic importing."""
    import importlib
    
    # List of modules to import dynamically
    modules_to_import = ['os', 'sys', 'json', 'math']
    imported_modules = {}
    
    for module_name in modules_to_import:
        try:
            # TODO: Use importlib to import module
            module = importlib.import_module(module_name)
            imported_modules[module_name] = module
            print(f"Successfully imported {module_name}")
            
            # TODO: Get module information
            if hasattr(module, '__file__'):
                print(f"  Location: {module.__file__}")
            if hasattr(module, '__version__'):
                print(f"  Version: {module.__version__}")
                
        except ImportError as e:
            print(f"Failed to import {module_name}: {e}")
    
    return imported_modules

def reload_module_demo():
    """Demonstrate module reloading."""
    import importlib
    
    try:
        # TODO: Import utils module if it exists
        import utils
        print(f"Original version: {utils.VERSION}")
        
        # TODO: Reload the module
        importlib.reload(utils)
        print("Module reloaded")
        
    except ImportError:
        print("utils module not found - create it first")

# Test dynamic imports
# dynamic_import_demo()
# reload_module_demo()

# TODO 7: Challenge - Plugin system
print(f"\n7. Challenge - Plugin System:")

class PluginManager:
    """Simple plugin management system."""
    
    def __init__(self, plugin_dir="plugins"):
        self.plugin_dir = Path(plugin_dir)
        self.plugins = {}
        self.plugin_dir.mkdir(exist_ok=True)
    
    def create_sample_plugins(self):
        """Create sample plugins for testing."""
        # Create plugin base class
        base_content = '''"""
Base plugin class.
"""

class BasePlugin:
    """Base class for all plugins."""
    
    def __init__(self):
        self.name = "Base Plugin"
        self.version = "1.0.0"
    
    def execute(self, data):
        """Execute plugin functionality."""
        raise NotImplementedError("Plugins must implement execute method")
    
    def get_info(self):
        """Get plugin information."""
        return {
            "name": self.name,
            "version": self.version
        }
'''
        
        # Create text processor plugin
        text_plugin_content = '''"""
Text processing plugin.
"""

from .base_plugin import BasePlugin

class TextProcessor(BasePlugin):
    def __init__(self):
        super().__init__()
        self.name = "Text Processor"
        self.version = "1.0.0"
    
    def execute(self, data):
        """Process text data."""
        if isinstance(data, str):
            return {
                "original": data,
                "uppercase": data.upper(),
                "word_count": len(data.split()),
                "char_count": len(data)
            }
        return {"error": "Data must be a string"}
'''
        
        # Create math processor plugin
        math_plugin_content = '''"""
Math processing plugin.
"""

from .base_plugin import BasePlugin

class MathProcessor(BasePlugin):
    def __init__(self):
        super().__init__()
        self.name = "Math Processor"
        self.version = "1.0.0"
    
    def execute(self, data):
        """Process numeric data."""
        if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
            return {
                "sum": sum(data),
                "average": sum(data) / len(data) if data else 0,
                "min": min(data) if data else None,
                "max": max(data) if data else None,
                "count": len(data)
            }
        return {"error": "Data must be a list of numbers"}
'''
        
        # TODO: Write plugin files
        (self.plugin_dir / "__init__.py").touch()
        
        with open(self.plugin_dir / "base_plugin.py", 'w') as f:
            f.write(base_content)
        
        with open(self.plugin_dir / "text_processor.py", 'w') as f:
            f.write(text_plugin_content)
        
        with open(self.plugin_dir / "math_processor.py", 'w') as f:
            f.write(math_plugin_content)
        
        print("Created sample plugins")
    
    def discover_plugins(self):
        """Discover and load plugins."""
        import importlib.util
        
        # TODO: Find all Python files in plugin directory
        plugin_files = list(self.plugin_dir.glob("*_processor.py"))
        
        for plugin_file in plugin_files:
            try:
                # TODO: Load module dynamically
                spec = importlib.util.spec_from_file_location(
                    plugin_file.stem, plugin_file
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # TODO: Find plugin classes
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if (isinstance(attr, type) and 
                        hasattr(attr, 'execute') and 
                        attr_name != 'BasePlugin'):
                        
                        plugin_instance = attr()
                        self.plugins[plugin_instance.name] = plugin_instance
                        print(f"Loaded plugin: {plugin_instance.name}")
                        
            except Exception as e:
                print(f"Failed to load {plugin_file}: {e}")
    
    def list_plugins(self):
        """List all loaded plugins."""
        return [plugin.get_info() for plugin in self.plugins.values()]
    
    def execute_plugin(self, plugin_name, data):
        """Execute a specific plugin."""
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].execute(data)
        else:
            return {"error": f"Plugin '{plugin_name}' not found"}

# Test plugin system
# plugin_manager = PluginManager()
# plugin_manager.create_sample_plugins()
# plugin_manager.discover_plugins()
# 
# print("Available plugins:")
# for plugin in plugin_manager.list_plugins():
#     print(f"  {plugin}")
# 
# # Test plugins
# text_result = plugin_manager.execute_plugin("Text Processor", "Hello World Python")
# math_result = plugin_manager.execute_plugin("Math Processor", [1, 2, 3, 4, 5])
# 
# print(f"Text processing result: {text_result}")
# print(f"Math processing result: {math_result}")

print(f"\n✅ Intermediate Exercise 4 complete! Check solutions/04_modules_packages_solution.py")

# Self-test questions:
"""
1. What's the difference between 'import module' and 'from module import function'?
2. When should you use relative vs absolute imports?
3. What is the purpose of __init__.py files?
4. How does Python find modules when you import them?
5. What's the difference between a module and a package?
"""