
# 1. SINGLE LEVEL INHERITANCE

# Q1. Create a parent class Father with house()
# and child class Son with bike().

class Father:
    def house(self):
        print("Father has a house")

class Son(Father):
    def bike(self):
        print("Son has a bike")

s = Son()
s.house()
s.bike()

# OUTPUT:
# Father has a house
# Son has a bike


# Q2. Create a parent class Person with show_name()
# and child class Student with show_roll().

class Person:
    def show_name(self):
        print("Name: Rahul")

class Student(Person):
    def show_roll(self):
        print("Roll No: 101")

s = Student()
s.show_name()
s.show_roll()

# OUTPUT:
# Name: Rahul
# Roll No: 101


# 2. METHOD CHAINING


# Q1. Create add(), sub() and mul() methods
# and call them using method chaining.

class Demo:
    def add(self):
        print("Addition")
        return self

    def sub(self):
        print("Subtraction")
        return self

    def mul(self):
        print("Multiplication")
        return self

d = Demo()
d.add().sub().mul()

# OUTPUT:
# Addition
# Subtraction
# Multiplication


# Q2. Create name(), salary() and role()
# methods using method chaining.

class Employee:
    def name(self):
        print("Name: Rahul")
        return self

    def salary(self):
        print("Salary: 25000")
        return self

    def role(self):
        print("Role: Developer")
        return self

e = Employee()
e.name().salary().role()

# OUTPUT:
# Name: Rahul
# Salary: 25000
# Role: Developer



# 3. CONSTRUCTOR CHAINING


# Q1. Call parent constructor from child constructor
# using super().

class Father:
    def __init__(self):
        print("Father Constructor")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Constructor")

s = Son()

# OUTPUT:
# Father Constructor
# Son Constructor


# Q2. Pass name and roll number using
# constructor chaining.

class Person:
    def __init__(self, name):
        self.name = name
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
        print("Roll No:", self.roll)

s = Student("Rahul", 101)

# OUTPUT:
# Name: Rahul
# Roll No: 101
