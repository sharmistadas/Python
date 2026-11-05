

# DEFINITION:
# Variable scope defines where a variable can be accessed
# and used in a Python program.

# ============================================================
# 1. LOCAL VARIABLE
# ============================================================

# DEFINITION:
# A variable created inside a function is called a local variable.
# It can be accessed only inside that function.

# Q1. Create a local variable and print it.
def student():
    name = "Rahul"
    print("Student Name:", name)

student()

# Output: Student Name: Rahul
# Explanation:
# name is created inside the function.
# So, it is a local variable and can be accessed inside student().


# Q2. Create two local variables and calculate their sum.
def add():
    a = 10
    b = 20
    print("Sum:", a + b)

add()

# Output: Sum: 30
# Explanation:
# a and b are local variables.
# They can be used only inside the add() function.


# Q3. Create a local variable inside a function.
def employee():
    salary = 30000
    print("Salary:", salary)

employee()

# Output: Salary: 30000
# Explanation:
# salary is created inside employee().
# It cannot be directly accessed outside the function.


# Q4. Create two functions with the same local variable name.
def first():
    x = 100
    print("First:", x)

def second():
    x = 200
    print("Second:", x)

first()
second()

# Output:
# First: 100
# Second: 200
# Explanation:
# Both functions have their own local variable x.
# Changing or creating x in one function does not affect the other.


# Q5. Check whether a local variable can be accessed outside.
def display():
    message = "Hello Python"
    print(message)

display()

# print(message)  # NameError

# Output:
# Hello Python
# Explanation:
# message is a local variable.
# It works inside display(), but cannot be accessed outside it.


# ============================================================
# 2. GLOBAL VARIABLE
# ============================================================

# DEFINITION:
# A variable created outside all functions is called a global variable.
# It can be accessed inside and outside functions.
# Use the global keyword to modify it inside a function.

# Q1. Create a global variable and access it inside a function.
name = "Riya"

def student():
    print("Student Name:", name)

student()

# Output: Student Name: Riya
# Explanation:
# name is created outside the function.
# Therefore, it is a global variable and can be accessed inside student().


# Q2. Access a global variable inside and outside a function.
college = "JSpiders"

def display():
    print("Inside Function:", college)

display()
print("Outside Function:", college)

# Output:
# Inside Function: JSpiders
# Outside Function: JSpiders
# Explanation:
# A global variable can be accessed both inside and outside functions.


# Q3. Modify a global variable using the global keyword.
count = 10

def update():
    global count
    count = 20
    print("Inside:", count)

update()
print("Outside:", count)

# Output:
# Inside: 20
# Outside: 20
# Explanation:
# global tells Python to modify the existing global variable,
# instead of creating a new local variable.


# Q4. Create a global variable and calculate its value.
price = 1000

def calculate():
    global price
    price = price + 500
    print("Updated Price:", price)

calculate()

# Output: Updated Price: 1500
# Explanation:
# price is a global variable.
# The global keyword allows us to update its value inside the function.


# Q5. Use a global variable in multiple functions.
balance = 5000

def deposit():
    global balance
    balance = balance + 2000
    print("After Deposit:", balance)

def withdraw():
    global balance
    balance = balance - 1000
    print("After Withdrawal:", balance)

deposit()
withdraw()

# Output:
# After Deposit: 7000
# After Withdrawal: 6000
# Explanation:
# Both functions access and modify the same global variable balance.


# ============================================================
# 3. NONLOCAL VARIABLE
# ============================================================

# DEFINITION:
# A nonlocal variable is created in an enclosing (outer) function.
# It is used inside a nested (inner) function.
# The nonlocal keyword allows the inner function to modify
# the variable from the nearest enclosing function scope.
# It does not refer to a global variable.

# Q1. Access a nonlocal variable inside a nested function.
def outer():
    name = "Rahul"

    def inner():
        print("Name:", name)

    inner()

outer()

# Output: Name: Rahul
# Explanation:
# name is created in outer().
# inner() can access it because it is inside the outer function.


# Q2. Modify a nonlocal variable.
def outer():
    count = 10

    def inner():
        nonlocal count
        count = 20
        print("Inner:", count)

    inner()
    print("Outer:", count)

outer()

# Output:
# Inner: 20
# Outer: 20
# Explanation:
# nonlocal allows inner() to modify count from outer().
# Both print statements show the updated value.


# Q3. Increase a value using nonlocal.
def counter():
    number = 0

    def increment():
        nonlocal number
        number = number + 1
        print("Count:", number)

    increment()
    increment()
    increment()

counter()

# Output:
# Count: 1
# Count: 2
# Count: 3
# Explanation:
# Each time increment() runs, it updates the number
# variable belonging to counter().


# Q4. Create a shopping cart using nonlocal.
def shopping():
    total = 0

    def add_item(price):
        nonlocal total
        total = total + price
        print("Current Total:", total)

    add_item(100)
    add_item(200)
    add_item(300)

shopping()

# Output:
# Current Total: 100
# Current Total: 300
# Current Total: 600
# Explanation:
# total belongs to shopping().
# add_item() modifies the same total using nonlocal.


# Q5. Modify a student's marks using nonlocal.
def student():
    marks = 70

    def update_marks():
        nonlocal marks
        marks = marks + 20
        print("Updated Marks:", marks)

    update_marks()
    print("Final Marks:", marks)

student()

# Output:
# Updated Marks: 90
# Final Marks: 90
# Explanation:
# marks is created in the outer function.
# The inner function modifies it using nonlocal.


# ============================================================
# QUICK REVISION – DIFFERENCE BETWEEN 3 SCOPES
# ============================================================

# 1. LOCAL VARIABLE:
# Created inside a function.
# Accessible only within its function.

# 2. GLOBAL VARIABLE:
# Created outside all functions.
# Accessible inside and outside functions.
# Use global keyword to modify it inside a function.

# 3. NONLOCAL VARIABLE:
# Created inside an outer function.
# Used inside a nested inner function.
# Use nonlocal keyword to modify it.

# ============================================================
# IMPORTANT INTERVIEW QUESTIONS
# ============================================================

# Q1. What is a local variable?
# Answer: A variable created inside a function.

# Q2. What is a global variable?
# Answer: A variable created outside all functions.

# Q3. What is a nonlocal variable?
# Answer: A variable in an enclosing function scope
#         that can be accessed and modified by a nested function.

# Q4. What is the use of the global keyword?
# Answer: It allows us to modify a global variable inside a function.

# Q5. What is the use of the nonlocal keyword?
# Answer: It allows us to modify a variable from an enclosing function.

# Q6. Can we access a local variable outside its function?
# Answer: No, not directly.

# Q7. Can a global variable be accessed inside a function?
# Answer: Yes.

# Q8. Can we use nonlocal outside a nested function?
# Answer: No. It must refer to a variable in an enclosing function scope.

# END OF VARIABLE SCOPE NOTES
