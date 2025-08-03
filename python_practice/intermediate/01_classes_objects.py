#!/usr/bin/env python3
"""
Intermediate Exercise 1: Classes and Objects

Learn about object-oriented programming in Python.
Complete the TODOs to practice creating and using classes.
"""

print("=== Intermediate Exercise 1: Classes and Objects ===\n")

# TODO 1: Basic class definition
print("1. Basic Class Definition:")

class Person:
    """A simple Person class."""
    
    # TODO: Add class variable for species
    species = None  # All humans belong to "Homo sapiens"
    
    def __init__(self, name, age):
        """Initialize a Person instance."""
        # TODO: Set instance attributes
        self.name = None
        self.age = None
    
    def introduce(self):
        """Return an introduction string."""
        # TODO: Return a string like "Hi, I'm Alice and I'm 25 years old"
        pass
    
    def have_birthday(self):
        """Increase age by 1."""
        # TODO: Increment the age
        pass
    
    def is_adult(self):
        """Check if person is 18 or older."""
        # TODO: Return True if age >= 18, False otherwise
        pass

# Test the Person class
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 17)
# print(person1.introduce())
# print(f"Is {person1.name} an adult? {person1.is_adult()}")
# print(f"Is {person2.name} an adult? {person2.is_adult()}")
# person1.have_birthday()
# print(f"After birthday: {person1.introduce()}")

# TODO 2: Class with properties and validation
print(f"\n2. Properties and Validation:")

class BankAccount:
    """A bank account class with balance validation."""
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize a bank account."""
        self.account_holder = account_holder
        self._balance = 0  # Private attribute
        # TODO: Set initial balance using the deposit method
    
    @property
    def balance(self):
        """Get the current balance."""
        # TODO: Return the balance
        pass
    
    def deposit(self, amount):
        """Deposit money to the account."""
        # TODO: Validate amount > 0, then add to balance
        pass
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        # TODO: Validate amount > 0 and amount <= balance
        # Return True if successful, False if insufficient funds
        pass
    
    def transfer(self, other_account, amount):
        """Transfer money to another account."""
        # TODO: Withdraw from this account and deposit to other
        # Return True if successful, False otherwise
        pass
    
    def __str__(self):
        """String representation of the account."""
        # TODO: Return a string like "Account(Alice): $100.00"
        pass

# Test the BankAccount class
# alice_account = BankAccount("Alice", 1000)
# bob_account = BankAccount("Bob", 500)
# print(alice_account)
# print(bob_account)
# alice_account.withdraw(200)
# print(f"After withdrawal: {alice_account}")
# alice_account.transfer(bob_account, 300)
# print(f"After transfer - Alice: {alice_account}")
# print(f"After transfer - Bob: {bob_account}")

# TODO 3: Inheritance
print(f"\n3. Inheritance:")

class Animal:
    """Base Animal class."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
    
    def eat(self, food_energy=20):
        """Animal eats and gains energy."""
        self.energy += food_energy
        return f"{self.name} ate and gained {food_energy} energy"
    
    def sleep(self):
        """Animal sleeps and recovers energy."""
        self.energy = 100
        return f"{self.name} slept and is fully rested"
    
    def make_sound(self):
        """Base method for animal sounds."""
        return f"{self.name} makes a sound"

class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name, breed):
        # TODO: Call parent constructor with name and species="Canis lupus"
        self.breed = breed
        self.tricks = []
    
    def make_sound(self):
        """Override the parent method."""
        # TODO: Return a dog-specific sound
        pass
    
    def learn_trick(self, trick):
        """Dog learns a new trick."""
        # TODO: Add trick to tricks list
        pass
    
    def perform_trick(self, trick):
        """Dog performs a trick if known."""
        # TODO: Check if trick is known, return appropriate message
        pass

class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name, indoor=True):
        # TODO: Call parent constructor
        self.indoor = indoor
        self.lives = 9
    
    def make_sound(self):
        """Override the parent method."""
        # TODO: Return a cat-specific sound
        pass
    
    def climb(self):
        """Cat climbs and uses energy."""
        # TODO: Reduce energy by 10, return climb message
        pass

# Test inheritance
# dog = Dog("Buddy", "Golden Retriever")
# cat = Cat("Whiskers", indoor=True)
# print(dog.make_sound())
# print(cat.make_sound())
# dog.learn_trick("sit")
# dog.learn_trick("roll over")
# print(dog.perform_trick("sit"))
# print(dog.perform_trick("fetch"))  # Not learned

# TODO 4: Class methods and static methods
print(f"\n4. Class Methods and Static Methods:")

class Temperature:
    """Temperature class with conversion methods."""
    
    def __init__(self, celsius=0):
        self.celsius = celsius
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Create Temperature instance from Fahrenheit."""
        # TODO: Convert fahrenheit to celsius and create instance
        # Formula: C = (F - 32) * 5/9
        pass
    
    @classmethod
    def from_kelvin(cls, kelvin):
        """Create Temperature instance from Kelvin."""
        # TODO: Convert kelvin to celsius and create instance
        # Formula: C = K - 273.15
        pass
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        # TODO: Return fahrenheit value
        # Formula: F = C * 9/5 + 32
        pass
    
    @staticmethod
    def celsius_to_kelvin(celsius):
        """Convert Celsius to Kelvin."""
        # TODO: Return kelvin value
        # Formula: K = C + 273.15
        pass
    
    def to_fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return self.celsius_to_fahrenheit(self.celsius)
    
    def to_kelvin(self):
        """Get temperature in Kelvin."""
        return self.celsius_to_kelvin(self.celsius)
    
    def __str__(self):
        return f"{self.celsius}°C"

# Test Temperature class
# temp1 = Temperature(25)
# temp2 = Temperature.from_fahrenheit(77)
# temp3 = Temperature.from_kelvin(298.15)
# print(f"Temp1: {temp1} = {temp1.to_fahrenheit()}°F = {temp1.to_kelvin()}K")
# print(f"Temp2: {temp2}")
# print(f"Temp3: {temp3}")

# TODO 5: Magic methods (dunder methods)
print(f"\n5. Magic Methods:")

class Vector:
    """2D Vector class with magic methods."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer representation."""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Add two vectors."""
        # TODO: Return new Vector with sum of components
        pass
    
    def __sub__(self, other):
        """Subtract two vectors."""
        # TODO: Return new Vector with difference of components
        pass
    
    def __mul__(self, scalar):
        """Multiply vector by scalar."""
        # TODO: Return new Vector with scaled components
        pass
    
    def __eq__(self, other):
        """Check if two vectors are equal."""
        # TODO: Return True if both x and y components are equal
        pass
    
    def __len__(self):
        """Return the magnitude of the vector."""
        # TODO: Return the length using Pythagorean theorem
        # import math and use math.sqrt(x² + y²)
        pass
    
    def magnitude(self):
        """Return the magnitude of the vector."""
        return len(self)

# Test Vector class
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
# print(f"v1: {v1}")
# print(f"v2: {v2}")
# print(f"v1 + v2: {v1 + v2}")
# print(f"v1 - v2: {v1 - v2}")
# print(f"v1 * 2: {v1 * 2}")
# print(f"v1 == v2: {v1 == v2}")
# print(f"Length of v1: {len(v1)}")

# TODO 6: Challenge - Library Management System
print(f"\n6. Challenge - Library Management System:")

class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author, isbn, copies=1):
        # TODO: Initialize book attributes
        pass
    
    def __str__(self):
        # TODO: Return book description
        pass

class Library:
    """Library management system."""
    
    def __init__(self, name):
        self.name = name
        self.books = {}  # ISBN -> Book mapping
        self.borrowed_books = {}  # ISBN -> borrower_name mapping
    
    def add_book(self, book):
        """Add a book to the library."""
        # TODO: Add book to collection
        pass
    
    def remove_book(self, isbn):
        """Remove a book from the library."""
        # TODO: Remove book if it exists and isn't borrowed
        pass
    
    def borrow_book(self, isbn, borrower_name):
        """Borrow a book if available."""
        # TODO: Check availability and lend book
        pass
    
    def return_book(self, isbn):
        """Return a borrowed book."""
        # TODO: Return book to available collection
        pass
    
    def search_by_title(self, title):
        """Search for books by title."""
        # TODO: Return list of books with matching title
        pass
    
    def search_by_author(self, author):
        """Search for books by author."""
        # TODO: Return list of books by matching author
        pass
    
    def list_available_books(self):
        """List all available books."""
        # TODO: Return list of available books
        pass
    
    def list_borrowed_books(self):
        """List all borrowed books with borrower info."""
        # TODO: Return list of borrowed books
        pass

# Test the Library system
# library = Library("City Library")
# book1 = Book("Python Programming", "John Doe", "123456789")
# book2 = Book("Data Science", "Jane Smith", "987654321")
# library.add_book(book1)
# library.add_book(book2)
# print("Available books:", library.list_available_books())
# library.borrow_book("123456789", "Alice")
# print("After borrowing:", library.list_available_books())
# print("Borrowed books:", library.list_borrowed_books())

print(f"\n✅ Intermediate Exercise 1 complete! Check solutions/01_classes_objects_solution.py")

# Self-test questions:
"""
1. What's the difference between instance and class variables?
2. When would you use @property decorator?
3. What's the purpose of __init__ and __str__ methods?
4. How does inheritance work in Python?
5. What are magic methods and when should you use them?
"""