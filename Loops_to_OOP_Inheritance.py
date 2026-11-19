#Part 1: Loops (Q1–Q10)

# Q1. Print numbers from 1 to 10

for i in range(1, 11):
    print(i, end=" ")

# Output:
# 1 2 3 4 5 6 7 8 9 10


# Q2. Print even numbers from 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

# Output:
# 2 4 6 8 10 12 14 16 18 20


# Q3. Print odd numbers from 1 to 20

for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=" ")

# Output:
# 1 3 5 7 9 11 13 15 17 19


# Q4. Multiplication table

num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50


# Q5. Sum of numbers from 1 to 10

total = 0

for i in range(1, 11):
    total += i

print(f"Sum = {total}")

# Output:
# Sum = 55


# Q6. Factorial of a number

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print(f"Factorial = {fact}")

# Output:
# Factorial = 120


# Q7. Check prime number

num = 7
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print(f"{num} is Prime")
else:
    print(f"{num} is Not Prime")

# Output:
# 7 is Prime


# Q8. Reverse a number using while loop

num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(f"Reverse = {rev}")

# Output:
# Reverse = 4321


# Q9. Count digits in a number

num = 12345
count = 0

while num > 0:
    count += 1
    num //= 10

print(f"Number of digits = {count}")

# Output:
# Number of digits = 5


# Q10. Print star pattern

for i in range(1, 6):
    print("*" * i)

# Output:
# *
# **
# ***
# ****
# *****



#Part 2: Strings (Q11–Q15)


# Q11. Reverse a string without slicing

s = "Python"
rev = ""

for ch in s:
    rev = ch + rev

print(f"Reverse: {rev}")

# Output:
# Reverse: nohtyP


# Q12. Count vowels and consonants

s = "Python Programming"
vowels = 0
consonants = 0

for ch in s.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")

# Output:
# Vowels: 4
# Consonants: 12


# Q13. Check palindrome string

s = "madam"

if s == s[::-1]:
    print(f"{s} is Palindrome")
else:
    print(f"{s} is Not Palindrome")

# Output:
# madam is Palindrome


# Q14. Count uppercase, lowercase, digits
# and special characters

s = "PyThon@123"
upper = lower = digits = special = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")
print(f"Digits: {digits}")
print(f"Special: {special}")

# Output:
# Uppercase: 2
# Lowercase: 4
# Digits: 3
# Special: 1


# Q15. Count character frequency

s = "banana"

for ch in dict.fromkeys(s):
    print(f"{ch}: {s.count(ch)}")

# Output:
# b: 1
# a: 3
# n: 2


#Part 3: List (Q16–Q20)


# Q16. Find largest and smallest

numbers = [10, 50, 20, 5, 40]

print(f"Largest: {max(numbers)}")
print(f"Smallest: {min(numbers)}")

# Output:
# Largest: 50
# Smallest: 5


# Q17. Remove duplicate elements

numbers = [10, 20, 10, 30, 20, 40]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(f"Unique elements: {unique}")

# Output:
# Unique elements: [10, 20, 30, 40]


# Q18. Find second largest element

numbers = [10, 50, 20, 40, 30]

unique = sorted(set(numbers))

print(f"Second largest: {unique[-2]}")

# Output:
# Second largest: 40


# Q19. Separate even and odd numbers

numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"Even: {even}")
print(f"Odd: {odd}")

# Output:
# Even: [2, 4, 6]
# Odd: [1, 3, 5]


# Q20. Sort list without sort()

numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(f"Sorted list: {numbers}")

# Output:
# Sorted list: [1, 2, 3, 5, 8]


#Part 4: Tuple and Set (Q21–Q25)


# Q21. Find maximum, minimum and length

t = (10, 20, 30, 40, 50)

print(f"Maximum: {max(t)}")
print(f"Minimum: {min(t)}")
print(f"Length: {len(t)}")

# Output:
# Maximum: 50
# Minimum: 10
# Length: 5


# Q22. Count element occurrence in tuple

t = (10, 20, 10, 30, 10, 40)

print(f"10 occurs: {t.count(10)} times")

# Output:
# 10 occurs: 3 times


# Q23. Union, intersection and difference

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference: {a - b}")

# Output:
# Union: {10, 20, 30, 40, 50, 60}
# Intersection: {30, 40}
# Difference: {10, 20}


# Q24. Remove duplicates using set

numbers = [10, 20, 10, 30, 20]

result = list(set(numbers))

print(f"Unique: {sorted(result)}")

# Output:
# Unique: [10, 20, 30]


# Q25. Check subset

a = {10, 20}
b = {10, 20, 30, 40}

print(f"Is subset: {a.issubset(b)}")

# Output:
# Is subset: True

#Part 5: Dictionary (Q26–Q30)

# Q26. Student details using dictionary

student = {
    "name": "Arjun",
    "roll": 101,
    "marks": 85
}

print(f"Name: {student['name']}")
print(f"Roll: {student['roll']}")
print(f"Marks: {student['marks']}")

# Output:
# Name: Arjun
# Roll: 101
# Marks: 85


# Q27. Print all keys and values

student = {"name": "Arjun", "age": 22, "marks": 85}

for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: Arjun
# age: 22
# marks: 85


# Q28. Find key with maximum value

marks = {"Python": 90, "Java": 80, "SQL": 95}

highest = max(marks, key=marks.get)

print(f"Highest subject: {highest}")
print(f"Highest marks: {marks[highest]}")

# Output:
# Highest subject: SQL
# Highest marks: 95


# Q29. Word frequency

sentence = "python java python sql java python"
words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# Output:
# {'python': 3, 'java': 2, 'sql': 1}


# Q30. Merge two dictionaries

d1 = {"a": 10, "b": 20}
d2 = {"c": 30, "d": 40}

result = {**d1, **d2}

print(f"Merged: {result}")

# Output:
# Merged: {'a': 10, 'b': 20, 'c': 30, 'd': 40}

#Part 6: Functions (Q31–Q40)

# Q31. Function to print 1 to 10

def numbers():
    for i in range(1, 11):
        print(i, end=" ")

numbers()

# Output:
# 1 2 3 4 5 6 7 8 9 10


# Q32. Check even or odd using function

def check(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

check(10)
check(7)

# Output:
# 10 is Even
# 7 is Odd


# Q33. Function with arguments and return

def add(a, b):
    return a + b

result = add(10, 20)
print(f"Sum: {result}")

# Output:
# Sum: 30


# Q34. Factorial using function

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

print(f"Factorial: {factorial(5)}")

# Output:
# Factorial: 120


# Q35. Prime number using function

def prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(f"7 is Prime: {prime(7)}")
print(f"8 is Prime: {prime(8)}")

# Output:
# 7 is Prime: True
# 8 is Prime: False


# Q36. Four types of user-defined functions

# 1. Without argument and without return
def greet():
    print("Hello Python")

greet()


# 2. With argument and without return
def display(name):
    print(f"Name: {name}")

display("Arjun")


# 3. Without argument and with return
def get_age():
    return 24

age = get_age()
print(f"Age: {age}")


# 4. With argument and with return
def square(num):
    return num * num

print(f"Square: {square(5)}")

# Output:
# Hello Python
# Name: Arjun
# Age: 24
# Square: 25


# Q37. Use *args to calculate sum

def total(*args):
    return sum(args)

print(f"Total: {total(10, 20, 30, 40)}")

# Output:
# Total: 100


# Q38. Use **kwargs to display employee details

def employee(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

employee(name="Rahul", age=25, salary=30000)

# Output:
# name: Rahul
# age: 25
# salary: 30000


# Q39. Local, Global and Nonlocal variables

x = 100

def outer():
    y = 200

    def inner():
        nonlocal y
        y = 300
        print(f"Nonlocal: {y}")

    inner()
    print(f"Outer: {y}")

def show():
    x_local = 50
    print(f"Local: {x_local}")

outer()
show()
print(f"Global: {x}")

# Output:
# Nonlocal: 300
# Outer: 300
# Local: 50
# Global: 100


# Q40. Create a decorator

def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

@my_decorator
def display():
    print("Hello Python")

display()

# Output:
# Before execution
# Hello Python
# After execution

#Part 7: OOP Fundamentals (Q41–Q48)

# Q41. Student class and object

class Student:
    def display(self):
        print("Student Name: Arjun")
        print("Roll Number: 101")
        print("Marks: 85")

s1 = Student()
s1.display()

# Output:
# Student Name: Arjun
# Roll Number: 101
# Marks: 85


# Q42. Employee class using constructor

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

e1 = Employee("Rahul", 30000)
e1.display()

# Output:
# Name: Rahul
# Salary: 30000


# Q43. Bank Account

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print(f"Balance: ₹{self.balance}")

account = BankAccount(5000)
account.deposit(2000)
account.withdraw(1000)
account.check_balance()

# Output:
# Balance: ₹6000


# Q44. Rectangle area and perimeter

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(10, 5)

print(f"Area: {r.area()}")
print(f"Perimeter: {r.perimeter()}")

# Output:
# Area: 50
# Perimeter: 30


# Q45. Instance and class variables

class Employee:
    company = "Infosys"

    def __init__(self, name):
        self.name = name

e1 = Employee("Rahul")
e2 = Employee("Priya")

print(f"Employee 1: {e1.name}")
print(f"Employee 2: {e2.name}")
print(f"Company: {Employee.company}")

# Output:
# Employee 1: Rahul
# Employee 2: Priya
# Company: Infosys


# Q46. Instance, class and static methods

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print(f"Name: {self.name}")

    @classmethod
    def class_method(cls):
        print(f"School: {cls.school}")

    @staticmethod
    def static_method():
        print("Welcome to Python")

s = Student("Arjun")

s.instance_method()
Student.class_method()
Student.static_method()

# Output:
# Name: Arjun
# School: ABC School
# Welcome to Python


# Q47. Encapsulation using getter

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

s = Student("Arjun", 90)

print(f"Name: {s.get_name()}")
print(f"Marks: {s.get_marks()}")

# Output:
# Name: Arjun
# Marks: 90


# Q48. Getter and Setter

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")

e = Employee(25000)

print(f"Old Salary: {e.get_salary()}")

e.set_salary(35000)

print(f"New Salary: {e.get_salary()}")

# Output:
# Old Salary: 25000
# New Salary: 35000

#Part 8: Inheritance (Q49–Q56)

# Q49. Single Inheritance

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()
d.bark()

# Output:
# Animal is eating
# Dog is barking


# Q50. Constructor Chaining using super()

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show(self):
        self.display()
        print(f"Model: {self.model}")

c = Car("Maruti", "Swift")
c.show()

# Output:
# Brand: Maruti
# Model: Swift


# Q51. Method Overriding

class Employee:
    def display(self):
        print("Employee Details")

class Manager(Employee):
    def display(self):
        print("Manager Details")

m = Manager()
m.display()

# Output:
# Manager Details


# Q52. Multiple Inheritance

class Father:
    def father_property(self):
        print("Father: House")

class Mother:
    def mother_property(self):
        print("Mother: Gold")

class Child(Father, Mother):
    def child_property(self):
        print("Child: Education")

c = Child()
c.father_property()
c.mother_property()
c.child_property()

# Output:
# Father: House
# Mother: Gold
# Child: Education


# Q53. Multilevel Inheritance

class Grandfather:
    def house(self):
        print("Grandfather owns a house")

class Father(Grandfather):
    def car(self):
        print("Father owns a car")

class Son(Father):
    def bike(self):
        print("Son owns a bike")

s = Son()
s.house()
s.car()
s.bike()

# Output:
# Grandfather owns a house
# Father owns a car
# Son owns a bike


# Q54. Hierarchical Inheritance

class Parent:
    def display(self):
        print("Parent Class")

class Child1(Parent):
    def show1(self):
        print("Child 1")

class Child2(Parent):
    def show2(self):
        print("Child 2")

c1 = Child1()
c2 = Child2()

c1.display()
c1.show1()

c2.display()
c2.show2()

# Output:
# Parent Class
# Child 1
# Parent Class
# Child 2


# Q55. Method Chaining using super()

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
        super().show()

class C(B):
    def show(self):
        print("Class C")
        super().show()

obj = C()
obj.show()

# Output:
# Class C
# Class B
# Class A


# Q56. Method Overriding with different children

class Shape:
    def area(self):
        print("Calculating area")

class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print(f"Rectangle Area: {length * width}")

class Square(Shape):
    def area(self):
        side = 5
        print(f"Square Area: {side * side}")

r = Rectangle()
s = Square()

r.area()
s.area()

# Output:
# Rectangle Area: 50
# Square Area: 25
