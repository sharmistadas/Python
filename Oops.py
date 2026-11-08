
# PYTHON OOP - CLASS VARIABLES AND INSTANCE VARIABLES



# Q1. BASIC CLASS DEFINITION AND OBJECT ATTRIBUTE ACCESS

class Sample:
    a = 10
    b = 20

s = Sample()
s1 = Sample()

print("Q1: BASIC CLASS")
print(s.a, s.b)
print(s1.a, s1.b)
print(Sample)

# print(Sample.c)  # AttributeError
# print(s.c)       # AttributeError

# Output:
# 10 20
# 10 20
# <class '__main__.Sample'>



# Q2. MODIFYING AND ADDING CLASS VARIABLES USING CLASS NAME

class Sample:
    a = 10
    b = 20

s = Sample()
s1 = Sample()

print("\nQ2: CLASS VARIABLE MODIFICATION")
print(Sample.a, s.a, s1.a)
print(Sample.b, s.b, s1.b)

# Modifying class variable
Sample.a = 120
print(Sample.a, s.a, s1.a)

# Adding new class variable
Sample.c = "happy diwali"
print(Sample.c, s.c, s1.c)

# Output:
# 10 10 10
# 20 20 20
# 120 120 120
# happy diwali happy diwali happy diwali



# Q3. MODIFYING AND ADDING INSTANCE VARIABLES USING OBJECTS

class Sample:
    a = 10
    b = 20

obj = Sample()
obj1 = Sample()
obj2 = Sample()

print("\nQ3: INSTANCE VARIABLE MODIFICATION")

# Modifying a for obj only
obj.a = "python"
print(Sample.a, obj.a, obj1.a, obj2.a)

# Modifying b for obj2 only
obj2.b = "java"
print(Sample.b, obj.b, obj1.b, obj2.b)

# Adding c for obj1 only
obj1.c = "HTML"
print(obj1.c)

# print(Sample.c)  # AttributeError
# print(obj.c)     # AttributeError
# print(obj2.c)    # AttributeError

# Output:
# 10 python 10 10
# 20 20 20 java
# HTML


# Q4. INSPECTING NAMESPACES USING __dict__

class Sample:
    a = 10
    b = 20

obj = Sample()
obj2 = Sample()

print("\nQ4: DICTIONARY")

# Initially empty instance dictionaries
print(obj.__dict__)
print(obj2.__dict__)

# Adding class variable
Sample.c = "happy"

# Adding instance variables to obj
obj.a = "TEN"
obj.b = "twenty"
print(obj.__dict__)

# Adding instance variable to obj2
obj2.b = "twenty"
print(obj2.__dict__)

# Adding more instance variables to obj2
obj2.c = "johnson"
obj2.d = "baby"
obj2.e = "soap"
print(obj2.__dict__)

# Output:
# {}
# {}
# {'a': 'TEN', 'b': 'twenty'}
# {'b': 'twenty'}
# {'b': 'twenty', 'c': 'johnson', 'd': 'baby', 'e': 'soap'}



# Q5. EMPLOYEE CLASS AND EXTERNAL ATTRIBUTE CALCULATION

class Employee:
    name = "Nandini"
    cmp_name = "TCS"
    emp_id = 123892
    sal = 700000

print("\nQ5: EMPLOYEE DETAILS")

# Accessing class attributes
print(f"Employee Details\n"
      f"Company Name: {Employee.cmp_name}\n"
      f"Employee ID: {Employee.emp_id}\n"
      f"Employee Name: {Employee.name}\n"
      f"Current Salary: {Employee.sal}")

# Adding hike percentage
Employee.hike = 13

# Calculating revised salary
Employee.revised_sal = Employee.sal + (
    Employee.sal * Employee.hike / 100
)

print(f"Revised Salary: {Employee.revised_sal}")

# Output:
# Employee Details
# Company Name: TCS
# Employee ID: 123892
# Employee Name: Nandini
# Current Salary: 700000
# Revised Salary: 791000.0

