# ============================================================================
# TASK 1: PYTHON FUNCTIONS
# ============================================================================

# Example 1: Function definition and calling
def my_function():
    print("Hello from a function")

my_function()




# Example 2: Function with parameters (positional arguments)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")




# Example 3: Function with default argument
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()
welcome("Charlie")




# Example 4: Function with return statement
def add(a, b):
    return a + b

result = add(5, 10)
print(f"Sum: {result}")




# Example 5: Function with *args (variable number of positional arguments)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")


# ============================================================================
# TASK 2: PYTHON LAMBDA EXPRESSIONS
# ============================================================================

# Example 1: Basic lambda syntax
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")




# Example 2: Lambda with map() for transformation
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")




# Example 3: Lambda with filter() for selection
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")




# Example 4: Lambda with sorted() for custom sorting
students = [("Alice", 85), ("Bob", 75), ("Charlie", 90)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by score: {sorted_students}")


# ============================================================================
# TASK 3: PYTHON CLASSES AND OBJECTS
# ============================================================================

# Example 1: Class definition and object creation
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", 3)
dog1.bark()
print(f"Dog's name: {dog1.name}, Age: {dog1.age}")




# Example 2: Instance methods and the self parameter
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive(self):
        print(f"The {self.color} {self.brand} is driving...")
    
    def stop(self):
        print(f"The {self.color} {self.brand} stopped.")

car1 = Car("Tesla", "red")
car1.drive()
car1.stop()




# Example 3: Class variables vs instance variables
class Counter:
    count = 0  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
        Counter.count += 1
    
    def display(self):
        print(f"Name: {self.name}, Total objects: {Counter.count}")

c1 = Counter("First")
c1.display()
c2 = Counter("Second")
c2.display()




# Example 4: Modifying and deleting object properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("John", 30)
person.display()
person.age = 31
print(f"Modified age: {person.age}")


# ============================================================================
# TASK 4: PYTHON INHERITANCE
# ============================================================================

# Example 1: Parent and child class relationships
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

cat = Cat("Whiskers")
cat.speak()




# Example 2: Using super() to call parent methods
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def display(self):
        print(f"Brand: {self.brand}")

class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type
    
    def display(self):
        super().display()
        print(f"Type: {self.bike_type}")

bike = Bike("Yamaha", "Sports")
bike.display()




# Example 3: Method overriding
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.area()}")




# Example 4: Multiple inheritance
class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()
