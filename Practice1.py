#! Q1. WAP to check whether a number is positive and divisible by 5

num = int(input("Enter a number: "))

if num > 0 and num % 5 == 0:
    print("Valid number")

# OUTPUT 1: VALID DATA
# Enter a number: 40
# Valid number

# OUTPUT 2: INVALID DATA
# Enter a number: 87
# No output

#! Q2. WAP to check working age

age = int(input("Enter age: "))

if age >= 18 and age <= 60:
    print("Working age")

# OUTPUT 1: VALID DATA
# Enter age: 25
# Working age

# OUTPUT 2: INVALID DATA
# Enter age: 65
# No output

#! Q3. WAP to check acceptable password

password = input("Enter password: ")

if len(password) >= 8 and "@" in password:
    print("Acceptable password")

# OUTPUT 1: VALID DATA
# Enter password: python@123
# Acceptable password

# OUTPUT 2: INVALID DATA
# Enter password: python123
# No output


#! Q4. WAP to check examination eligibility

attendance = float(input("Enter attendance percentage: "))

if attendance >= 75:
    print("Eligible for examination")

# OUTPUT 1: VALID DATA
# Enter attendance percentage: 80
# Eligible for examination

# OUTPUT 2: INVALID DATA
# Enter attendance percentage: 60
# No output

#! Q5. WAP to check product availability

products = {
    "laptop": 10,
    "mouse": 5,
    "keyboard": 0
}

product = input("Enter product name: ")

if product in products and products[product] > 0:
    print("Product available")

# OUTPUT 1: VALID DATA
# Enter product name: laptop
# Product available

# OUTPUT 2: INVALID DATA
# Enter product name: keyboard
# No output


#! Q6. WAP to check course availability

courses = ["Python", "Java", "SQL", "React"]

course = input("Enter course name: ")

if course in courses:
    print("Registration available")

# OUTPUT 1: VALID DATA
# Enter course name: Python
# Registration available

# OUTPUT 2: INVALID DATA
# Enter course name: C++
# No output