# Q1. WAP TO CHECK WHETHER THE DATA IS MUTABLE OR IMMUTABLE

data = eval(input("Enter the data: "))

if type(data) in (list, set, dict):
    print("Mutable")
else:
    print("Immutable")

# TRUE OUTPUT:
# Enter the data: [10, 20, 30]
# Mutable
#
# FALSE OUTPUT:
# Enter the data: 10
# Immutable


# Q2. WAP TO CHECK WHETHER A NUMBER IS EVEN OR ODD

num = int(input("Enter the number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# TRUE OUTPUT:
# Enter the number: 6
# Even
#
# FALSE OUTPUT:
# Enter the number: 9
# Odd


# Q3. WAP TO CHECK WHETHER THE GIVEN STRING IS A CHARACTER

s = input("Enter the string: ")

if len(s) == 1:
    print(f"{s} is a character")
else:
    print("It is not a character")

# TRUE OUTPUT:
# Enter the string: g
# g is a character
#
# FALSE OUTPUT:
# Enter the string: hello
# It is not a character


# Q4. WAP TO CHECK WHETHER A CHARACTER IS A VOWEL OR CONSONANT

s = input("Enter the character: ")

if s.upper() in "AEIOU":
    print(f"{s} is a vowel")
else:
    print(f"{s} is a consonant")

# TRUE OUTPUT:
# Enter the character: a
# a is a vowel
#
# FALSE OUTPUT:
# Enter the character: b
# b is a consonant

 
# Q5. WAP TO CHECK WHETHER DATA IS SINGLE VALUE OR COLLECTION

data = [10, 20, 30]

if type(data) == list:
    print("Collection")
else:
    print("Single value data")

# TRUE OUTPUT:
# Collection


# Q6. WAP TO PRINT THE MIDDLE CHARACTER OF THE STRING IF THE STRING HAS MIDDLE CHARACTER

s = input("Enter a string: ")

if len(s) % 2 != 0:
    print("Middle character:", s[len(s) // 2])
else:
    print("No single middle character")

# TRUE OUTPUT:
# Enter a string: hello
# Middle character: l
#
# FALSE OUTPUT:
# Enter a string: python
# No single middle character


# Q7. WAP TO CHECK WHETHER A NUMBER IS POSITIVE OR NEGATIVE

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
else:
    print("Negative number")

# TRUE OUTPUT:
# Enter a number: 8
# Positive number
#
# FALSE OUTPUT:
# Enter a number: -9
# Negative number



# Q8. WAP TO CHECK WHETHER A TUPLE IS HOMOGENEOUS OR HETEROGENEOUS

t = (10, 20)

if type(t[0]) == type(t[1]):
    print("Homogeneous tuple")
else:
    print("Heterogeneous tuple")

# TRUE OUTPUT:
# Homogeneous tuple
#
# FALSE OUTPUT:
# If t = (10, "hello")
# Heterogeneous tuple


# Q9. WAP TO CHECK WHETHER TWO VALUES ARE EQUAL OR NOT

a = 10
b = 10

if a == b:
    print("Both are equal")
else:
    print("Both are not equal")

# TRUE OUTPUT:
# Both are equal
#
# FALSE OUTPUT:
# If a = 10 and b = 20
# Both are not equal


# Q10. WAP TO PRINT SQUARE OF EVEN NUMBER AND CUBE OF ODD NUMBER

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