

# DEFINITION:
# Arguments are values passed to a function during a function call.
# They provide input to a function to perform a particular task.

# ============================================================
# 1. POSITIONAL ARGUMENTS
# ============================================================
# Definition:
# Arguments passed according to the position of parameters.
# The order of arguments is important.

# Q1. Display student name and age.
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Rahul", 22)
# Output: Name: Rahul, Age: 22
# Explanation: Rahul goes to name and 22 goes to age.

# Q2. Add two numbers.
def add(a, b):
    print("Sum:", a + b)

add(10, 20)
# Output: Sum: 30
# Explanation: 10 is assigned to a and 20 to b.

# Q3. Calculate the area of a rectangle.
def area(length, breadth):
    print("Area:", length * breadth)

area(10, 5)
# Output: Area: 50
# Explanation: Values are assigned according to their positions.

# Q4. Display employee details.
def employee(name, salary, city):
    print(name, salary, city)

employee("Amit", 30000, "Hyderabad")
# Output: Amit 30000 Hyderabad
# Explanation: Three arguments are assigned to three parameters in order.

# Q5. Find the average of three numbers.
def average(a, b, c):
    print("Average:", (a + b + c) / 3)

average(10, 20, 30)
# Output: Average: 20.0
# Explanation: All three positional values are used to calculate the average.


# ============================================================
# 2. KEYWORD ARGUMENTS
# ============================================================
# Definition:
# Arguments passed using parameter names.
# The order of arguments does not matter.

# Q1. Display student details.
def student(name, age):
    print(name, age)

student(age=22, name="Riya")
# Output: Riya 22
# Explanation: Values are assigned using parameter names.

# Q2. Add two numbers.
def add(a, b):
    print("Sum:", a + b)

add(b=20, a=10)
# Output: Sum: 30
# Explanation: The order does not matter because keywords are used.

# Q3. Calculate rectangle area.
def area(length, breadth):
    print("Area:", length * breadth)

area(breadth=5, length=10)
# Output: Area: 50
# Explanation: Each value is assigned to its named parameter.

# Q4. Display employee details.
def employee(name, salary, city):
    print(name, salary, city)

employee(city="Hyderabad", name="Amit", salary=30000)
# Output: Amit 30000 Hyderabad
# Explanation: Arguments can be passed in any order using keywords.

# Q5. Calculate total marks.
def total_marks(english, maths, science):
    print("Total:", english + maths + science)

total_marks(science=80, english=90, maths=85)
# Output: Total: 255
# Explanation: Each subject's marks are assigned by parameter name.


# ============================================================
# 3. COMBINATION OF POSITIONAL AND KEYWORD ARGUMENTS
# ============================================================
# Definition:
# Passing positional and keyword arguments in the same function call.
# Positional arguments must come before keyword arguments.

# Q1. Display student details.
def student(name, age, course):
    print(name, age, course)

student("Rahul", age=22, course="Python")
# Output: Rahul 22 Python
# Explanation: Rahul is positional; age and course are keyword arguments.

# Q2. Calculate employee salary.
def salary(name, basic, bonus):
    print(name, "Total Salary:", basic + bonus)

salary("Amit", bonus=5000, basic=25000)
# Output: Amit Total Salary: 30000
# Explanation: Name is positional and the remaining values are keywords.

# Q3. Calculate rectangle area.
def area(length, breadth):
    print("Area:", length * breadth)

area(10, breadth=5)
# Output: Area: 50
# Explanation: Length is positional and breadth is keyword-based.

# Q4. Display product details.
def product(name, price, quantity):
    print(name, price * quantity)

product("Laptop", quantity=2, price=50000)
# Output: Laptop 100000
# Explanation: Product name is positional; price and quantity are keywords.

# Q5. Calculate final marks.
def marks(name, subject, score):
    print(name, subject, score)

marks("Riya", score=95, subject="Python")
# Output: Riya Python 95
# Explanation: Name is positional; score and subject are keyword arguments.


# ============================================================
# 4. POSITIONAL-ONLY ARGUMENTS (/)
# ============================================================
# Definition:
# Parameters before / accept only positional arguments.
# We cannot pass them using keyword names.

# Q1. Add two numbers.
def add(a, b, /):
    print("Sum:", a + b)

add(10, 20)
# Output: Sum: 30
# Explanation: Both parameters must receive values by position.

# Q2. Divide two numbers.
def divide(a, b, /):
    print("Division:", a / b)

divide(20, 5)
# Output: Division: 4.0
# Explanation: a and b are positional-only parameters.

# Q3. Display student details.
def student(name, age, /):
    print(name, age)

student("Riya", 22)
# Output: Riya 22
# Explanation: Both values must be passed according to their positions.

# Q4. Calculate rectangle area.
def area(length, breadth, /):
    print("Area:", length * breadth)

area(10, 5)
# Output: Area: 50
# Explanation: Values cannot be passed using length=10 or breadth=5.

# Q5. Calculate simple interest.
def interest(p, r, t, /):
    print("Simple Interest:", (p * r * t) / 100)

interest(10000, 5, 2)
# Output: Simple Interest: 1000.0
# Explanation: All three parameters accept positional values only.


# ============================================================
# 5. KEYWORD-ONLY ARGUMENTS (*)
# ============================================================
# Definition:
# Parameters after * accept only keyword arguments.
# Values must be passed using parameter names.

# Q1. Display student details.
def student(*, name, age):
    print(name, age)

student(name="Riya", age=22)
# Output: Riya 22
# Explanation: Both arguments must be passed using keywords.

# Q2. Calculate total price.
def total(*, price, quantity):
    print("Total:", price * quantity)

total(price=100, quantity=5)
# Output: Total: 500
# Explanation: Price and quantity are keyword-only parameters.

# Q3. Calculate employee salary.
def salary(*, basic, bonus):
    print("Salary:", basic + bonus)

salary(basic=25000, bonus=5000)
# Output: Salary: 30000
# Explanation: Values must be passed using parameter names.

# Q4. Display product information.
def product(*, name, price, brand):
    print(name, price, brand)

product(name="Mobile", price=15000, brand="Samsung")
# Output: Mobile 15000 Samsung
# Explanation: All parameters are keyword-only.

# Q5. Calculate rectangle area.
def area(*, length, breadth):
    print("Area:", length * breadth)

area(length=10, breadth=5)
# Output: Area: 50
# Explanation: Both values must be passed as keyword arguments.


# ============================================================
# 6. COMBINATION OF POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS
# ============================================================
# Definition:
# A function can contain positional-only and keyword-only parameters.
# / separates positional-only parameters.
# * separates keyword-only parameters.

# Q1. Display employee details.
def employee(name, age, /, *, salary, city):
    print(name, age, salary, city)

employee("Amit", 24, salary=30000, city="Hyderabad")
# Output: Amit 24 30000 Hyderabad
# Explanation: Name and age are positional-only; salary and city are keyword-only.

# Q2. Calculate student total marks.
def marks(name, /, *, maths, science):
    print(name, maths + science)

marks("Riya", maths=90, science=85)
# Output: Riya 175
# Explanation: Name is positional-only; subject marks are keyword-only.

# Q3. Calculate product total.
def product(name, /, *, price, quantity):
    print(name, price * quantity)

product("Laptop", price=50000, quantity=2)
# Output: Laptop 100000
# Explanation: Name must be positional; price and quantity must be keywords.

# Q4. Calculate simple interest.
def interest(p, r, /, *, t):
    print("Interest:", (p * r * t) / 100)

interest(10000, 5, t=2)
# Output: Interest: 1000.0
# Explanation: Principal and rate are positional-only; time is keyword-only.

# Q5. Display course details.
def course(name, duration, /, *, fees, mode):
    print(name, duration, fees, mode)

course("Python", "6 Months", fees=25000, mode="Offline")
# Output: Python 6 Months 25000 Offline
# Explanation: Name and duration are positional-only; fees and mode are keyword-only.


# ============================================================
# 7. VARIABLE-LENGTH KEYWORD ARGUMENTS (**kwargs)
# ============================================================
# Definition:
# **kwargs accepts any number of keyword arguments.
# Python stores them in a dictionary.

# Q1. Display student details.
def student(**kwargs):
    print(kwargs)

student(name="Riya", age=22, course="Python")
# Output: {'name': 'Riya', 'age': 22, 'course': 'Python'}
# Explanation: All keyword arguments are stored in a dictionary.

# Q2. Display employee details one by one.
def employee(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee(name="Amit", salary=30000, city="Hyderabad")
# Output:
# name : Amit
# salary : 30000
# city : Hyderabad
# Explanation: items() returns dictionary keys and values.

# Q3. Calculate total marks.
def marks(**kwargs):
    print("Total:", sum(kwargs.values()))

marks(english=80, maths=90, science=85)
# Output: Total: 255
# Explanation: values() returns all dictionary values.

# Q4. Display product information.
def product(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

product(name="Mobile", price=15000, brand="Samsung")
# Output:
# name = Mobile
# price = 15000
# brand = Samsung
# Explanation: We can pass any number of named values.

# Q5. Calculate total expenses.
def expenses(**kwargs):
    print("Total Expenses:", sum(kwargs.values()))

expenses(food=2000, travel=1500, shopping=3000)
# Output: Total Expenses: 6500
# Explanation: All keyword values are stored in a dictionary and added.


# ============================================================
# 8. VARIABLE-LENGTH POSITIONAL ARGUMENTS (*args)
# ============================================================
# Definition:
# *args accepts any number of positional arguments.
# Python stores them in a tuple.

# Q1. Add multiple numbers.
def add(*args):
    print("Sum:", sum(args))

add(10, 20, 30, 40)
# Output: Sum: 100
# Explanation: All positional values are collected into a tuple.

# Q2. Find the maximum number.
def maximum(*args):
    print("Maximum:", max(args))

maximum(10, 50, 30, 80, 20)
# Output: Maximum: 80
# Explanation: max() returns the largest tuple value.

# Q3. Find the minimum number.
def minimum(*args):
    print("Minimum:", min(args))

minimum(10, 50, 5, 80, 20)
# Output: Minimum: 5
# Explanation: min() returns the smallest value.

# Q4. Display all student names.
def students(*args):
    for name in args:
        print(name)

students("Rahul", "Riya", "Amit")
# Output:
# Rahul
# Riya
# Amit
# Explanation: The loop accesses each value from the tuple.

# Q5. Calculate average marks.
def average(*args):
    print("Average:", sum(args) / len(args))

average(80, 90, 70, 100)
# Output: Average: 85.0
# Explanation: sum() adds all marks and len() counts the values.


# ============================================================
# 9. COMBINATION OF *args AND **kwargs
# ============================================================
# Definition:
# A function can accept both variable-length positional arguments
# and variable-length keyword arguments.
# *args stores values in a tuple.
# **kwargs stores values in a dictionary.
# *args must come before **kwargs in the function definition.

# Q1. Display student information.
def student(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

student("Riya", 22, course="Python", city="Hyderabad")
# Output:
# Positional: ('Riya', 22)
# Keyword: {'course': 'Python', 'city': 'Hyderabad'}
# Explanation: Positional values go into args and named values into kwargs.

# Q2. Calculate total of positional numbers.
def add(*args, **kwargs):
    print("Sum:", sum(args))
    print("Details:", kwargs)

add(10, 20, 30, subject="Maths", name="Rahul")
# Output:
# Sum: 60
# Details: {'subject': 'Maths', 'name': 'Rahul'}
# Explanation: Numbers are collected in args; extra named details in kwargs.

# Q3. Display employee information.
def employee(*args, **kwargs):
    print("Basic Details:", args)
    print("Additional Details:", kwargs)

employee("Amit", 25, salary=30000, city="Hyderabad")
# Output:
# Basic Details: ('Amit', 25)
# Additional Details: {'salary': 30000, 'city': 'Hyderabad'}
# Explanation: Both types of variable-length arguments are accepted.

# Q4. Calculate marks and display student details.
def result(*args, **kwargs):
    print("Total Marks:", sum(args))
    print("Student Details:", kwargs)

result(80, 90, 85, name="Riya", course="Python")
# Output:
# Total Marks: 255
# Student Details: {'name': 'Riya', 'course': 'Python'}
# Explanation: Marks are positional values; name and course are keywords.

# Q5. Calculate shopping total.
def shopping(*args, **kwargs):
    print("Total Price:", sum(args))
    print("Product Details:", kwargs)

shopping(1000, 2000, 500, customer="Rahul", payment="UPI")
# Output:
# Total Price: 3500
# Product Details: {'customer': 'Rahul', 'payment': 'UPI'}
# Explanation: Prices are stored in a tuple and customer details in a dictionary.


# ============================================================
# 10. DEFAULT ARGUMENTS
# ============================================================
# Definition:
# Default arguments are parameters that already have a default value.
# If the caller does not provide a value, Python uses the default value.
# Parameters with default values must come after non-default parameters.

# Q1. Display student details with a default city.
def student(name, city="Hyderabad"):
    print(name, city)

student("Riya")
# Output: Riya Hyderabad
# Explanation: City uses its default value because no city was passed.

# Q2. Calculate power with a default exponent.
def power(number, exponent=2):
    print("Result:", number ** exponent)

power(5)
# Output: Result: 25
# Explanation: Exponent is 2 by default, so 5 is squared.

# Q3. Calculate employee salary with default bonus.
def salary(basic, bonus=2000):
    print("Total Salary:", basic + bonus)

salary(25000)
# Output: Total Salary: 27000
# Explanation: If bonus is not provided, Python uses 2000.

# Q4. Display course details with default duration.
def course(name, duration="6 Months"):
    print(name, duration)

course("Python")
# Output: Python 6 Months
# Explanation: Duration uses its default value.

# Q5. Calculate rectangle area with a default breadth.
def area(length, breadth=5):
    print("Area:", length * breadth)

area(10)
# Output: Area: 50
# Explanation: Length is provided as 10; breadth uses its default value 5.


# ============================================================
# QUICK REVISION – ALL 10 TYPES
# ============================================================
# 1. Positional Arguments       : Values passed according to position.
# 2. Keyword Arguments          : Values passed using parameter names.
# 3. Positional + Keyword       : Both used in one function call.
# 4. Positional-Only            : Uses / separator.
# 5. Keyword-Only               : Uses * separator.
# 6. Positional-Only + Keyword-Only: Uses / and * separators.
# 7. Variable-Length Keyword   : **kwargs – stores values in dictionary.
# 8. Variable-Length Positional: *args – stores values in tuple.
# 9. *args + **kwargs           : Accepts both variable-length types.
# 10. Default Arguments         : Uses predefined values if not supplied.


# ============================================================
# IMPORTANT INTERVIEW QUESTIONS
# ============================================================
# Q1. What is the difference between *args and **kwargs?
# Answer:
# *args stores multiple positional arguments in a tuple.
# **kwargs stores multiple keyword arguments in a dictionary.

# Q2. What is the difference between positional and keyword arguments?
# Answer:
# Positional arguments depend on order.
# Keyword arguments depend on parameter names.

# Q3. What is the use of / in Python?
# Answer:
# It makes parameters positional-only.

# Q4. What is the use of * in Python?
# Answer:
# A standalone * makes following parameters keyword-only.

# Q5. What is a default argument?
# Answer:
# A parameter with a predefined value that is used
# when the caller does not provide an argument.

# Q6. Can positional arguments come after keyword arguments?
# Answer:
# No. Positional arguments must come before keyword arguments.

# Q7. Which data type is used by *args and **kwargs?
# Answer:
# *args = Tuple
# **kwargs = Dictionary

# Q8. Can we use *args and **kwargs together?
# Answer:
# Yes. *args must come before **kwargs in the function definition.

# END OF PYTHON ARGUMENTS NOTES
