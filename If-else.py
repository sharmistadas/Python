# Q1. WAP TO CHECK WHETHER DATA IS SINGLE VALUE OR COLLECTION

data = input("Enter data: ")

if type(data) in (int, float, str):
    print("Single value data")
else:
    print("Collection")

# OUTPUT:
# Enter data: hello
# Single value data
#
# True Output:
# Enter data: 100
# Single value data
#
# False Output:
# Enter data: [10, 20, 30]
# Collection


# Q2. WAP TO PRINT THE MIDDLE CHARACTER OF THE STRING IF THE STRING HAS A MIDDLE CHARACTER

s = input("Enter a string: ")

if len(s) % 2 != 0:
    middle = len(s) // 2
    print("Middle character:", s[middle])
else:
    print("String does not have a single middle character")

# OUTPUT:
# Enter a string: hello
# Middle character: l
#
# True Output:
# Enter a string: python
# String does not have a single middle character


# Q3. WAP TO CHECK WHETHER A NUMBER IS POSITIVE OR NEGATIVE

num = int(input("Enter the number: "))

if num > 0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")

# OUTPUT:
# Enter the number: 8
# 8 is a positive number
#
# True Output:
# Enter the number: 8
# 8 is a positive number
#
# False Output:
# Enter the number: -9
# -9 is a negative number
#
# NOTE:
# Here 0 will also be considered negative.
# Better version is given below:
#
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# Q4. WAP TO CHECK WHETHER A TUPLE IS HOMOGENEOUS OR HETEROGENEOUS

t = (10, 'hello')

if type(t[0]) == type(t[1]):
    print("Homogeneous tuple")
else:
    print("Heterogeneous tuple")

# TRUE OUTPUT:
# t = (10, 20)
# Homogeneous tuple
#
# FALSE OUTPUT:
# t = (10, 'hello')
# Heterogeneous tuple


# Q5. WAP TO CHECK WHETHER TWO VALUES ARE EQUAL OR NOT

a = 10
b = 50

if a == b:
    print("a and b are equal")
else:
    print("a and b are not equal")

# TRUE OUTPUT:
# a = 10
# b = 10
# a and b are equal
#
# FALSE OUTPUT:
# a = 10
# b = 50
# a and b are not equal


# Q6. WAP TO PRINT SQUARE OF EVEN NUMBER AND CUBE OF ODD NUMBER

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Square:", num ** 2)
else:
    print("Cube:", num ** 3)

# TRUE OUTPUT:
# Enter a number: 4
# Square: 16
#
# FALSE OUTPUT:
# Enter a number: 5
# Cube: 125