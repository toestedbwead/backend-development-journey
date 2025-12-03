# Object-Oriented Programming (OOP) in Python

## What is OOP?

**Object-Oriented Programming** is a programming paradigm that organizes code around **objects** - things that bundle data and behavior together.

Instead of having separate variables and functions, OOP groups related data and functions into objects.

---

## Core Concepts

### 1. Classes and Objects

**Class** = Blueprint/template for creating objects
**Object** = Instance created from a class

```python
# Class definition (blueprint)
class Car:
    pass

# Creating objects (instances)
car1 = Car()  # First car
car2 = Car()  # Second car (separate from car1)
```

**Analogy:**
- Class = Cookie cutter (blueprint)
- Object = Actual cookie (made from the blueprint)

---

### 2. The `__init__` Method (Constructor)

`__init__` is a special method that runs automatically when you create a new object. It's used to set up the object's initial data.

```python
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.fuel = 100  # Default value

# When you create an object:
my_car = Car("red", "Toyota")  # __init__ runs automatically
# my_car.color = "red"
# my_car.brand = "Toyota"
# my_car.fuel = 100
```

**Key points:**
- Always has `self` as first parameter
- Runs once when object is created
- Sets up initial data (attributes)

---

### 3. `self` - The Most Important Concept

`self` refers to **the specific object** that's calling the method.

**Why we need it:**

```python
class Car:
    def __init__(self, color):
        self.color = color
    
    def paint(self, new_color):
        self.color = new_color  # Which car's color? THIS car's color

# Two separate cars
car1 = Car("red")
car2 = Car("blue")

car1.paint("green")  # Changes car1's color only
# car1.color = "green"
# car2.color = "blue" (unchanged)
```

**Rules:**
- Always first parameter in methods
- Use it to access object's data: `self.attribute`
- Only exists inside class methods
- Outside the class, use object name: `car1.color`, not `self.color`

---

### 4. Attributes (Object Data)

**Attributes** = Variables that belong to an object

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # Attribute
        self.age = age        # Attribute
        self.is_adult = age >= 18  # Computed attribute

person = Person("Alice", 25)
print(person.name)      # Access attribute
person.age = 26         # Modify attribute
```

---

### 5. Methods (Object Functions)

**Methods** = Functions that belong to a class

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):      # Method
        self.balance += amount
    
    def withdraw(self, amount):     # Method
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):          # Method
        return self.balance

# Using methods
account = BankAccount(1000)
account.deposit(500)        # balance = 1500
account.withdraw(200)       # balance = 1300
print(account.get_balance())  # 1300
```

**Key points:**
- Always have `self` as first parameter
- Can access and modify object's attributes
- Can call other methods: `self.other_method()`

---

## Complete Example: Game Character

```python
import random

class GameCharacter:
    def __init__(self, name, health=100):
        """Initialize a new character"""
        self.name = name
        self.health = health
        self.max_health = health
        self.level = 1
    
    def take_damage(self, damage):
        """Reduce health by damage amount"""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage! Health: {self.health}")
    
    def heal(self, amount):
        """Restore health"""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} healed {amount}! Health: {self.health}")
    
    def is_alive(self):
        """Check if character is still alive"""
        return self.health > 0
    
    def level_up(self):
        """Increase level and max health"""
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        print(f"{self.name} leveled up to {self.level}!")

# Creating and using characters
hero = GameCharacter("Hero", 120)
enemy = GameCharacter("Goblin", 50)

hero.take_damage(30)        # Hero took 30 damage! Health: 90
hero.heal(20)               # Hero healed 20! Health: 110
hero.level_up()             # Hero leveled up to 2!

if hero.is_alive():
    print(f"{hero.name} is still fighting!")
```

---

## OOP vs Procedural Programming

### Procedural (functions and variables separate):

```python
# Data
player_health = 100
player_name = "Hero"
enemy_health = 50

# Functions
def take_damage(current_health, damage):
    return current_health - damage

def is_alive(health):
    return health > 0

# Using them
player_health = take_damage(player_health, 30)
if is_alive(player_health):
    print("Still alive")
```

**Problems:**
- Data and functions are separate
- Have to pass data everywhere
- Easy to lose track of related data
- Hard to manage multiple players

### Object-Oriented (data and functions bundled):

```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_damage(self, damage):
        self.health -= damage
    
    def is_alive(self):
        return self.health > 0

# Using it
player = Character("Hero", 100)
enemy = Character("Goblin", 50)

player.take_damage(30)
if player.is_alive():
    print("Still alive")
```

**Benefits:**
- Data and behavior together
- Each object manages its own data
- Can have multiple objects easily
- More organized and maintainable

---

## Key OOP Principles

### 1. Encapsulation
Bundle related data and methods together in a class.

```python
class EmailValidator:
    def __init__(self):
        self.valid_domains = ["gmail.com", "yahoo.com"]
    
    def is_valid(self, email):
        domain = email.split("@")[1]
        return domain in self.valid_domains
```

### 2. Separation of Concerns
Each class should have one clear responsibility.

```python
# Good - separate concerns
class GameEngine:
    def check_guess(self, guess):
        return "correct"  # Just logic

class UI:
    def display_message(self, message):
        print(message)  # Just display

# Bad - mixed concerns
class Game:
    def check_guess(self, guess):
        result = "correct"
        print(f"Result: {result}")  # Logic + display mixed!
```

---

## Common Patterns

### Pattern 1: Managing State

```python
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    
    def get_tasks(self):
        return self.tasks.copy()

todo = TodoList()
todo.add_task("Learn OOP")
todo.add_task("Build project")
```

### Pattern 2: Data Validation

```python
class User:
    def __init__(self, username, age):
        self.username = username
        self.set_age(age)
    
    def set_age(self, age):
        if age < 0 or age > 150:
            raise ValueError("Invalid age")
        self.age = age

user = User("Alice", 25)
# user = User("Bob", -5)  # Raises error
```

### Pattern 3: Configuration Objects

```python
class DatabaseConfig:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
    
    def get_connection_string(self):
        return f"{self.host}:{self.port}@{self.username}"

config = DatabaseConfig("localhost", 5432, "admin")
```

---

## When to Use Classes vs Functions

### Use Functions When:
- Simple, standalone operations
- No state to manage
- Pure calculations

```python
def calculate_tax(amount, rate):
    return amount * rate
```

### Use Classes When:
- Need to store and manage state
- Multiple related operations on the same data
- Creating multiple instances with different data

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_total(self):
        return sum(item.price for item in self.items)
```

---

## Common Mistakes and How to Avoid Them

### Mistake 1: Forgetting `self`

```python
# ❌ Wrong
class Car:
    def __init__(self, color):
        color = color  # Doesn't save to object!
    
    def get_color(self):
        return color  # Error: 'color' not defined

# ✅ Correct
class Car:
    def __init__(self, color):
        self.color = color  # Saves to object
    
    def get_color(self):
        return self.color  # Accesses object's data
```

### Mistake 2: Using Class Name Instead of `self`

```python
# ❌ Wrong
class GameEngine:
    def __init__(self):
        GameEngine.score = 0  # Don't do this!
    
    def add_points(self, points):
        GameEngine.score += points  # Wrong!

# ✅ Correct
class GameEngine:
    def __init__(self):
        self.score = 0  # Use self
    
    def add_points(self, points):
        self.score += points  # Use self
```

### Mistake 3: Not Returning Values

```python
# ❌ Wrong - modifies but doesn't help caller know
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, x, y):
        self.result = x + y  # Stores but doesn't return

# ✅ Better - return the result
class Calculator:
    def add(self, x, y):
        return x + y  # Caller can use the result
```

---

## Practice Exercises

### Exercise 1: Bank Account
Create a `BankAccount` class with:
- `__init__` that sets initial balance
- `deposit(amount)` method
- `withdraw(amount)` method (check sufficient funds)
- `get_balance()` method

### Exercise 2: Book Library
Create a `Library` class with:
- List of books (store as list of strings)
- `add_book(title)` method
- `remove_book(title)` method
- `search_book(title)` method that returns True/False

### Exercise 3: Temperature Converter
Create a `Temperature` class with:
- `__init__` that takes temperature in Celsius
- `to_fahrenheit()` method
- `to_kelvin()` method
- `set_celsius(temp)` method

---

## Summary

**Object-Oriented Programming** lets you:
- ✅ Bundle related data and functions together
- ✅ Create multiple independent objects from one class
- ✅ Organize code in a more maintainable way
- ✅ Model real-world concepts naturally

**Key concepts:**
- **Class**: Blueprint for creating objects
- **Object**: Instance created from a class
- **`__init__`**: Constructor that sets up new objects
- **`self`**: Reference to the current object
- **Attributes**: Data stored in objects
- **Methods**: Functions that belong to objects

**Remember:**
- Use `self` in all method definitions
- Use `self.attribute` to access object data
- Each object has its own independent data
- Methods can modify object state using `self`