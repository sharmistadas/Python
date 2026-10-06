# PYTHON IF AND IF-ELSE PRACTICE
# QUESTION + ANSWER + EXPLANATION + OUTPUTS


# SECTION 1: SIMPLE IF


# Q1. POSITIVE AND DIVISIBLE

# QUESTION:
# Input a number. If the number is positive and divisible by 5,
# display "Valid number".


# EXPLANATION:
# num > 0 checks whether the number is positive.
# num % 5 == 0 checks whether the number is divisible by 5.
# 'and' means BOTH conditions must be True.

num = int(input("Enter a number: "))

if num > 0 and num % 5 == 0:
    print("Valid number")


# OUTPUT 1: VALID DATA
# Enter a number: 40
# Valid number

# OUTPUT 2: INVALID DATA
# Enter a number: 87
# No output


# Q2. AGE VERIFICATION

# QUESTION:
# Input a person's age. If the age is between 18 and 60,
# display "Working age".

# EXPLANATION:
# age >= 18 checks that age is 18 or above.
# age <= 60 checks that age is 60 or below.
# Both conditions must be True.

age = int(input("Enter age: "))

if age >= 18 and age <= 60:
    print("Working age")


# OUTPUT 1: VALID DATA
# Enter age: 25
# Working age

# OUTPUT 2: INVALID DATA
# Enter age: 15
# No output


# Q3. PASSWORD STRENGTH
# QUESTION:
# Input a password. If its length is at least 8 characters
# and it contains "@", display "Acceptable password".

# EXPLANATION:
# len(password) >= 8 checks the password length.
# "@" in password checks whether @ is present.
# Both conditions must be True.

password = input("Enter password: ")

if len(password) >= 8 and "@" in password:
    print("Acceptable password")


# OUTPUT 1: VALID DATA
# Enter password: hello@123
# Acceptable password

# OUTPUT 2: INVALID DATA
# Enter password: hello123
# No output


# Q4. STUDENT ATTENDANCE
# QUESTION:
# Input a student's attendance percentage.
# If attendance is 75 or above,
# display "Eligible for examination".

# EXPLANATION:
# attendance >= 75 means attendance must be 75 or more.

attendance = float(input("Enter attendance percentage: "))

if attendance >= 75:
    print("Eligible for examination")


# OUTPUT 1: VALID DATA
# Enter attendance percentage: 80
# Eligible for examination

# OUTPUT 2: INVALID DATA
# Enter attendance percentage: 60
# No output


# Q5. PRODUCT AVAILABILITY
# QUESTION:
# Create a dictionary containing product names and stock
# quantities.
# Ask the user to enter a product name.
# If the product exists and stock is greater than 0,
# display "Product available".


# EXPLANATION:
# product in products checks whether the product exists.
# products[product] > 0 checks whether stock is available.
# Both conditions must be True.

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


# Q6. COURSE REGISTRATION
# QUESTION:
# Create a list containing available course names.
# Ask the user to enter a course name.
# If the course is available,
# display "Registration available".

# EXPLANATION:
# course in courses checks whether the course exists
# inside the list.

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


# ============================================================
# Q7. LOGIN STATUS
# ============================================================
# QUESTION:
# Create the Boolean variables:
# is_logged_in = True
# is_verified = True
#
# If both conditions are true,
# display "Access granted".
#
# EXPLANATION:
# True means the condition is correct.
# 'and' means both conditions must be True.

is_logged_in = True
is_verified = True

if is_logged_in and is_verified:
    print("Access granted")


# OUTPUT 1: VALID DATA
# Access granted

# OUTPUT 2: INVALID DATA
# is_logged_in = False
# is_verified = True
# No output


# ============================================================
# Q8. WEEKEND ACTIVITY
# ============================================================
# QUESTION:
# Ask the user to enter a day.
# If the day is "Saturday" or "Sunday",
# display "Weekend".
#
# EXPLANATION:
# == is used to compare values.
# 'or' means at least ONE condition should be True.

day = input("Enter day: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")


# OUTPUT 1: VALID DATA
# Enter day: Saturday
# Weekend

# OUTPUT 2: INVALID DATA
# Enter day: Monday
# No output


# ============================================================
# Q9. VALID DISCOUNT CODE
# ============================================================
# QUESTION:
# Create a set containing valid discount codes.
# Ask the user to enter a discount code.
# If the code exists in the set and the user is logged in,
# display "Discount applied".
#
# EXPLANATION:
# code in discount_codes checks whether the code is valid.
# is_logged_in checks whether the user is logged in.
# Both conditions must be True.

discount_codes = {"SAVE10", "SAVE20", "SALE50"}

code = input("Enter discount code: ")

is_logged_in = True

if code in discount_codes and is_logged_in:
    print("Discount applied")


# OUTPUT 1: VALID DATA
# Enter discount code: SAVE10
# Discount applied

# OUTPUT 2: INVALID DATA
# Enter discount code: ABC10
# No output


# ============================================================
# Q10. EMPLOYEE ACCESS
# ============================================================
# QUESTION:
# Create variables for role and account_status.
# If role is "admin" and account_status is "active",
# display "Full access granted".
#
# EXPLANATION:
# role == "admin" checks the employee role.
# account_status == "active" checks account status.
# Both conditions must be True.

role = input("Enter role: ")
account_status = input("Enter account status: ")

if role == "admin" and account_status == "active":
    print("Full access granted")


# OUTPUT 1: VALID DATA
# Enter role: admin
# Enter account status: active
# Full access granted

# OUTPUT 2: INVALID DATA
# Enter role: user
# Enter account status: active
# No output


# ============================================================
# SECTION 2: IF-ELSE
# ============================================================


# ============================================================
# Q11. EXAM RESULT
# ============================================================
# QUESTION:
# Input marks.
# If marks are between 40 and 100, display "Pass".
# Otherwise display "Fail".
# If marks are outside 0-100, display "Invalid marks".
#
# EXPLANATION:
# First check whether marks are invalid.
# marks < 0 means marks are below 0.
# marks > 100 means marks are above 100.
#
# If marks are 40 or above, print Pass.
# Otherwise, print Fail.

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


# OUTPUT 1: VALID DATA
# Enter marks: 80
# Pass

# OUTPUT 2: INVALID DATA
# Enter marks: 25
# Fail

# OUTPUT 3: INVALID RANGE
# Enter marks: 110
# Invalid marks


# ============================================================
# Q12. NUMBER VALIDATION
# ============================================================
# QUESTION:
# Input a number.
# If the number is positive and even,
# display "Valid".
# Otherwise display "Invalid".
#
# EXPLANATION:
# num > 0 checks whether the number is positive.
# num % 2 == 0 checks whether the number is even.
# Both conditions must be True.

num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("Valid")
else:
    print("Invalid")


# OUTPUT 1: VALID DATA
# Enter a number: 20
# Valid

# OUTPUT 2: INVALID DATA
# Enter a number: 15
# Invalid


# ============================================================
# Q13. LOGIN SYSTEM
# ============================================================
# QUESTION:
# Store a correct username and password.
# Ask the user to enter the username and password.
# If both are correct, display "Login successful".
# Otherwise display "Invalid credentials".
#
# EXPLANATION:
# correct_username stores the correct username.
# correct_password stores the correct password.
# == compares values.
# 'and' means BOTH username and password must be correct.

correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid credentials")


# OUTPUT 1: VALID DATA
# Enter username: admin
# Enter password: 1234
# Login successful

# OUTPUT 2: INVALID DATA
# Enter username: user
# Enter password: 1234
# Invalid credentials


# ============================================================
# IMPORTANT CONCEPTS
# ============================================================

# AND
# Both conditions must be True.
#
# Example:
# if age >= 18 and age <= 60:


# OR
# At least one condition must be True.
#
# Example:
# if day == "Saturday" or day == "Sunday":


# ==
# Used to COMPARE two values.
#
# Example:
# if username == "admin":


# %
# Modulus operator.
# It gives the remainder.
#
# Example:
# num % 2 == 0
# Means the number is EVEN.
#
# Example:
# num % 5 == 0
# Means the number is DIVISIBLE BY 5.


# IN
# Checks whether a value exists inside a collection.
#
# Example:
# if "Python" in courses:


# LEN()
# Counts the number of characters.
#
# Example:
# len(password) >= 8


# ============================================================
# SIMPLE IF STRUCTURE
# ============================================================

# if condition:
#     statement


# Example:

# num = int(input("Enter number: "))
#
# if num > 0:
#     print("Positive")


# ============================================================
# IF-ELSE STRUCTURE
# ============================================================

# if condition:
#     statement for True
# else:
#     statement for False


# Example:

# num = int(input("Enter number: "))
#
# if num > 0:
#     print("Positive")
# else:
#     print("Not positive")

