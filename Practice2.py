#! NESTED IF PROGRAMS


#! Q1. WAP to check whether a number is positive. If positive, check whether it is greater than 100.

num = int(input("Enter a number: "))

if num > 0:
    if num > 100:
        print("Positive and greater than 100")
    else:
        print("Positive but not greater than 100")
else:
    print("Number is not positive")


# OUTPUT 1: VALID DATA
# Enter a number: 150  
# Positive and greater than 100

# OUTPUT 2: INVALID DATA
# Enter a number: -20
# Number is not positive


#! Q2. Accept shopping amount. If amount is ₹1000 or more, check whether it is ₹5000 or more and give the appropriate discount.


amount = int(input("Enter shopping amount: "))

if amount >= 1000:
    if amount >= 5000:
        print("20% discount")
    else:
        print("10% discount")
else:
    print("No discount")


# OUTPUT 1: VALID DATA
# Enter shopping amount: 6000
# 20% discount

# OUTPUT 2: INVALID DATA
# Enter shopping amount: 500
# No discount


#! Q3. Check whether a number is even. If it is even, check whether it is divisible by 4.

num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 4 == 0:
        print("Even and divisible by 4")
    else:
        print("Even but not divisible by 4")
else:
    print("Number is odd")


# OUTPUT 1: VALID DATA
# Enter a number: 20
# Even and divisible by 4

# OUTPUT 2: INVALID DATA
# Enter a number: 15
# Number is odd


#! Q4. Accept a person's age. If age is 18+, check whether age is 60+ and print "Senior Citizen" or "Adult".

age = int(input("Enter age: "))

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Not eligible as adult")


# OUTPUT 1: VALID DATA
# Enter age: 65
# Senior Citizen

# OUTPUT 2: INVALID DATA
# Enter age: 16
# Not eligible as adult


#! Q5. Accept three subject marks. If the student passes all subjects,  check whether the average is above 75.


m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    average = (m1 + m2 + m3) / 3

    if average > 75:
        print("Passed all subjects and average is above 75")
    else:
        print("Passed all subjects but average is not above 75")
else:
    print("Student failed")


# OUTPUT 1: VALID DATA
# Enter subject 1 marks: 80
# Enter subject 2 marks: 85
# Enter subject 3 marks: 90
# Passed all subjects and average is above 75

# OUTPUT 2: INVALID DATA
# Enter subject 1 marks: 80
# Enter subject 2 marks: 35
# Enter subject 3 marks: 90
# Student failed


#! Q6. Accept a username.
# If correct, check the password.
# If password is correct, print "Login successful".


username = input("Enter username: ")

if username == "admin":
    password = input("Enter password: ")

    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")


# OUTPUT 1: VALID DATA
# Enter username: admin
# Enter password: 1234
# Login successful

# OUTPUT 2: INVALID DATA
# Enter username: admin
# Enter password: 5678
# Incorrect password


#! Q7. Accept a number.
# If it is positive, check whether it is single-digit,
# double-digit, or greater than 99.

num = int(input("Enter a number: "))

if num > 0:
    if num <= 9:
        print("Single-digit number")
    elif num <= 99:
        print("Double-digit number")
    else:
        print("Number is greater than 99")
else:
    print("Number is not positive")


# OUTPUT 1: VALID DATA
# Enter a number: 7
# Single-digit number

# OUTPUT 2: INVALID DATA
# Enter a number: -25
# Number is not positive


#! Q8. Accept salary.
# If salary is above ₹30,000,
# check whether it is above ₹60,000.


salary = int(input("Enter salary: "))

if salary > 30000:
    if salary > 60000:
        print("Salary is above 60000")
    else:
        print("Salary is above 30000 but not above 60000")
else:
    print("Salary is 30000 or below")


# OUTPUT 1: VALID DATA
# Enter salary: 75000
# Salary is above 60000

# OUTPUT 2: INVALID DATA
# Enter salary: 25000
# Salary is 30000 or below