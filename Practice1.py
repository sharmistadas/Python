
# SECTION 1 — SIMPLE IF


# Q1. POSITIVE AND DIVISIBLE

# QUESTION:
# Input a number.
# If the number is positive and divisible by 5,
# display "Valid number".


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
# Input a person's age.
# If the age is between 18 and 60,
# display "Working age".


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
# If password length is at least 8 characters
# and it contains @, display "Acceptable password".


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
# If attendance is 75 or above,
# display "Eligible for examination".


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
# Create a dictionary containing product names and stock.
# If product exists and stock is greater than 0,
# display "Product available".


products = {
    "laptop": 5,
    "mouse": 0,
    "keyboard": 3
}

product = input("Enter product name: ")

if product in products and products[product] > 0:
    print("Product available")


# OUTPUT 1: VALID DATA
# Enter product name: laptop
# Product available

# OUTPUT 2: INVALID DATA
# Enter product name: mouse
# No output


# Q6. COURSE REGISTRATION

# QUESTION:
# Create a list of available courses.
# If the course is available,
# display "Registration available".


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


# Q7. LOGIN STATUS

# QUESTION:
# Create:
# is_logged_in = True
# is_verified = True
# If both are True, display "Access granted".


is_logged_in = True
is_verified = True

if is_logged_in and is_verified:
    print("Access granted")


# OUTPUT 1: VALID DATA
# is_logged_in = True
# is_verified = True
# Access granted

# OUTPUT 2: INVALID DATA
# is_logged_in = False
# is_verified = True
# No output


# Q8. WEEKEND ACTIVITY

# QUESTION:
# If the entered day is Saturday or Sunday,
# display "Weekend".


day = input("Enter day: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")


# OUTPUT 1: VALID DATA
# Enter day: Saturday
# Weekend

# OUTPUT 2: INVALID DATA
# Enter day: Monday
# No output


# Q9. VALID DISCOUNT CODE

# QUESTION:
# If the discount code exists and the user is logged in,
# display "Discount applied".


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



# Q10. EMPLOYEE ACCESS

# QUESTION:
# If role is admin and account status is active,
# display "Full access granted".


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



# SECTION 2 — IF-ELSE


# Q11. EXAM RESULT

# QUESTION:
# 40–100 → Pass
# Otherwise → Fail
# Outside 0–100 → Invalid marks


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



# Q12. NUMBER VALIDATION

# QUESTION:
# If number is positive and even → Valid
# Otherwise → Invalid


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



# Q13. LOGIN SYSTEM

# QUESTION:
# Store correct username and password.
# If both are correct → Login successful.
# Otherwise → Invalid credentials.

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



# Q14. FILE DOWNLOAD

# QUESTION:
# Ask whether the user is logged in and whether the file
# is public.
# Allow download if user is logged in OR file is public.


is_logged_in = input("Is user logged in? ")

is_public = input("Is file public? ")

if is_logged_in == "yes" or is_public == "yes":
    print("Download allowed")
else:
    print("Download not allowed")


# OUTPUT 1: VALID DATA
# Is user logged in? yes
# Is file public? no
# Download allowed

# OUTPUT 2: INVALID DATA
# Is user logged in? no
# Is file public? no
# Download not allowed


# Q15. SHOPPING DISCOUNT

# QUESTION:
# Give discount only if customer is a member
# AND purchase amount is at least 2000.


amount = float(input("Enter purchase amount: "))
membership = input("Are you a member? ")

if membership == "yes" and amount >= 2000:
    print("Discount available")
else:
    print("No discount")


# OUTPUT 1: VALID DATA
# Enter purchase amount: 2500
# Are you a member? yes
# Discount available

# OUTPUT 2: INVALID DATA
# Enter purchase amount: 1500
# Are you a member? yes
# No discount


# Q16. LIBRARY ACCESS

# QUESTION:
# Student can borrow a book only when:
# 1. Student is a library member.
# 2. Account is active.


membership = input("Are you a library member? ")
account_status = input("Enter account status: ")

if membership == "yes" and account_status == "active":
    print("Book borrowing allowed")
else:
    print("Book borrowing not allowed")


# OUTPUT 1: VALID DATA
# Are you a library member? yes
# Enter account status: active
# Book borrowing allowed

# OUTPUT 2: INVALID DATA
# Are you a library member? no
# Enter account status: active
# Book borrowing not allowed



# Q17. USERNAME VALIDATION

# QUESTION:
# Accept username only if:
# 1. It is not empty.
# 2. Length is at least 5.
# 3. It does not contain spaces.


username = input("Enter username: ")

if username != "" and len(username) >= 5 and " " not in username:
    print("Valid username")
else:
    print("Invalid username")


# OUTPUT 1: VALID DATA
# Enter username: sharmi
# Valid username

# OUTPUT 2: INVALID DATA
# Enter username: sh
# Invalid username



# Q18. ATM WITHDRAWAL

# QUESTION:
# Allow withdrawal only if:
# 1. Amount > 0
# 2. Amount <= balance
# 3. Amount is a multiple of 100


balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount > 0 and amount <= balance and amount % 100 == 0:
    print("Withdrawal allowed")
else:
    print("Withdrawal not allowed")


# OUTPUT 1: VALID DATA
# Enter account balance: 10000
# Enter withdrawal amount: 2000
# Withdrawal allowed

# OUTPUT 2: INVALID DATA
# Enter account balance: 10000
# Enter withdrawal amount: 2500
# Withdrawal not allowed



# Q19. ONLINE COURSE ACCESS

# QUESTION:
# Ask whether user is logged in and enrolled.
# Allow access only when both are True.
#
# EXPLANATION:
# 'and' means both conditions must be True.

is_logged_in = input("Is user logged in? ")
is_enrolled = input("Is user enrolled? ")

if is_logged_in == "yes" and is_enrolled == "yes":
    print("Access granted")
else:
    print("Access denied")


# OUTPUT 1: VALID DATA
# Is user logged in? yes
# Is user enrolled? yes
# Access granted

# OUTPUT 2: INVALID DATA
# Is user logged in? yes
# Is user enrolled? no
# Access denied



# Q20. PRODUCT PURCHASE

# QUESTION:
# Given products and stock.
# If product exists and stock is available,
# display "Purchase allowed".



products = {
    "laptop": 5,
    "mouse": 0,
    "keyboard": 3
}

product = input("Enter product name: ")

if product in products and products[product] > 0:
    print("Purchase allowed")
else:
    print("Purchase not allowed")


# OUTPUT 1: VALID DATA
# Enter product name: laptop
# Purchase allowed

# OUTPUT 2: INVALID DATA
# Enter product name: mouse
# Purchase not allowed



# SECTION 3 — IF-ELIF-ELSE


# Q21. STUDENT GRADE

# QUESTION:
# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# 40–59 → E
# Below 40 → F
# Outside 0–100 → Invalid percentage


percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage")
elif percentage >= 90:
    print("A")
elif percentage >= 80:
    print("B")
elif percentage >= 70:
    print("C")
elif percentage >= 60:
    print("D")
elif percentage >= 40:
    print("E")
else:
    print("F")


# OUTPUT 1: VALID DATA
# Enter percentage: 92
# A

# OUTPUT 2: INVALID DATA
# Enter percentage: 35
# F

# OUTPUT 3: INVALID RANGE
# Enter percentage: 105
# Invalid percentage


# Q22. AGE CATEGORY

# QUESTION:
# Below 5 → Free
# 5–12 → Child
# 13–59 → Adult
# 60 and above → Senior Citizen
# Handle invalid ages.


age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Free")
elif age <= 12:
    print("Child")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")


# OUTPUT 1: VALID DATA
# Enter age: 10
# Child

# OUTPUT 2: INVALID DATA
# Enter age: -5
# Invalid age



# Q23. CHARACTER ANALYZER

# QUESTION:
# Input one character.
# Determine whether it is:
# Uppercase
# Lowercase
# Digit
# Special character
# If more than one character is entered → Invalid input.


ch = input("Enter one character: ")

if len(ch) != 1:
    print("Invalid input")
elif ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")


# OUTPUT 1: VALID DATA
# Enter one character: A
# Uppercase letter

# OUTPUT 2: INVALID DATA
# Enter one character: Hello
# Invalid input



# Q24. TRAFFIC SIGNAL

# QUESTION:
# red → Stop
# yellow → Wait
# green → Go
# Anything else → Invalid color


color = input("Enter traffic color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid color")


# OUTPUT 1: VALID DATA
# Enter traffic color: green
# Go

# OUTPUT 2: INVALID DATA
# Enter traffic color: blue
# Invalid color


# Q25. INTERNET USAGE

# QUESTION:
# 0–10 GB → Light User
# 11–50 GB → Normal User
# 51–100 GB → Heavy User


usage = float(input("Enter internet usage in GB: "))

if usage < 0 or usage > 100:
    print("Invalid usage")
elif usage <= 10:
    print("Light User")
elif usage <= 50:
    print("Normal User")
else:
    print("Heavy User")


# OUTPUT 1: VALID DATA
# Enter internet usage in GB: 25
# Normal User

# OUTPUT 2: INVALID DATA
# Enter internet usage in GB: 120
# Invalid usage


# Q26. EMPLOYEE EXPERIENCE

# QUESTION:
# Input years of experience and display the appropriate
# experience level.
#
# CONDITIONS USED:
# 0–1 years → Fresher
# 2–4 years → Junior
# 5–9 years → Experienced
# 10+ years → Senior


experience = int(input("Enter years of experience: "))

if experience < 0:
    print("Invalid experience")
elif experience <= 1:
    print("Fresher")
elif experience <= 4:
    print("Junior")
elif experience <= 9:
    print("Experienced")
else:
    print("Senior")


# OUTPUT 1: VALID DATA
# Enter years of experience: 3
# Junior

# OUTPUT 2: INVALID DATA
# Enter years of experience: -2
# Invalid experience



# Q27. ORDER STATUS

# QUESTION:
# Input order status and display the corresponding
# message/category.
#
# CONDITIONS USED:
# pending → Order is pending
# shipped → Order is shipped
# delivered → Order delivered
# cancelled → Order cancelled


status = input("Enter order status: ")

if status == "pending":
    print("Order is pending")
elif status == "shipped":
    print("Order is shipped")
elif status == "delivered":
    print("Order delivered")
elif status == "cancelled":
    print("Order cancelled")
else:
    print("Invalid status")


# OUTPUT 1: VALID DATA
# Enter order status: shipped
# Order is shipped

# OUTPUT 2: INVALID DATA
# Enter order status: processing
# Invalid status


# Q28. MOBILE DATA PLAN

# QUESTION:
# Input mobile data usage/requirement and display
# the appropriate plan.
#
# CONDITIONS USED:
# 0–2 GB → Basic Plan
# 3–10 GB → Standard Plan
# 11–30 GB → Premium Plan
# Above 30 GB → Unlimited Plan


data = float(input("Enter required data in GB: "))

if data < 0:
    print("Invalid data")
elif data <= 2:
    print("Basic Plan")
elif data <= 10:
    print("Standard Plan")
elif data <= 30:
    print("Premium Plan")
else:
    print("Unlimited Plan")


# OUTPUT 1: VALID DATA
# Enter required data in GB: 8
# Standard Plan

# OUTPUT 2: INVALID DATA
# Enter required data in GB: -5
# Invalid data


# Q29. PERFORMANCE LEVEL

# QUESTION:
# Input performance values and determine:
# Excellent
# Good
# Average
# Needs Improvement
#
# CONDITIONS USED:
# Performance is based on score and attendance.
#
# Excellent:
# score >= 90 AND attendance >= 90
#
# Good:
# score >= 75 AND attendance >= 75
#
# Average:
# score >= 50 AND attendance >= 50
#
# Otherwise:
# Needs Improvement


score = float(input("Enter performance score: "))
attendance = float(input("Enter attendance percentage: "))

if score >= 90 and attendance >= 90:
    print("Excellent")
elif score >= 75 and attendance >= 75:
    print("Good")
elif score >= 50 and attendance >= 50:
    print("Average")
else:
    print("Needs Improvement")


# OUTPUT 1: VALID DATA
# Enter performance score: 92
# Enter attendance percentage: 95
# Excellent

# OUTPUT 2: INVALID DATA
# Enter performance score: 40
# Enter attendance percentage: 45
# Needs Improvement


# Q!30. EMPLOYEE ACCESS LEVEL

# QUESTION:
# Ask the user to enter employee role:
# intern
# employee
# manager
# admin
# Display the corresponding access level.
# If role is not recognized → Invalid role.


role = input("Enter employee role: ")

if role == "intern":
    print("Limited access")
elif role == "employee":
    print("Basic access")
elif role == "manager":
    print("Manager access")
elif role == "admin":
    print("Full access")
else:
    print("Invalid role")


# OUTPUT 1: VALID DATA
# Enter employee role: manager
# Manager access

# OUTPUT 2: INVALID DATA
# Enter employee role: student
# Invalid role
