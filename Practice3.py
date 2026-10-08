
#!              NESTED IF - PRACTICE QUESTIONS 


#! Q1. SECURE LOGIN
#
# QUESTION:
# Create a login system:
# Ask for username.
# If username is correct, ask for password.
# If password is correct, ask for OTP.
# If OTP is correct, display "Login successful".
# Display an appropriate error message for each failure.


username = input("Enter username: ")

if username == "admin":
    password = input("Enter password: ")

    if password == "1234":
        otp = input("Enter OTP: ")

        if otp == "5678":
            print("Login successful")
        else:
            print("Incorrect OTP")
    else:
        print("Incorrect password")
else:
    print("Invalid username")


# OUTPUT 1: VALID DATA
# Enter username: admin
# Enter password: 1234
# Enter OTP: 5678
# Login successful

# OUTPUT 2: INVALID DATA
# Enter username: admin
# Enter password: 9999
# Incorrect password

# EXPLANATION:
# First username is checked.
# If username is correct, password is checked.
# If password is correct, OTP is checked.
# If all three are correct, login is successful.


#! Q2. EXAMINATION ELIGIBILITY
#
# QUESTION:
# Input:
# Attendance percentage
# Fee payment status
# ID card availability
#
# Check in order:
# 1. Attendance is sufficient.
# 2. Fee is paid.
# 3. ID card is available.
# 4. Allow the student to enter the examination only if
#    all conditions are satisfied.


attendance = int(input("Enter attendance percentage: "))
fee_paid = input("Is fee paid? (yes/no): ")
id_card = input("Is ID card available? (yes/no): ")

if attendance >= 75:

    if fee_paid == "yes":

        if id_card == "yes":
            print("Allowed to enter examination")
        else:
            print("ID card is not available")

    else:
        print("Fee is not paid")

else:
    print("Attendance is insufficient")


# OUTPUT 1: VALID DATA
# Enter attendance percentage: 85
# Is fee paid? (yes/no): yes
# Is ID card available? (yes/no): yes
# Allowed to enter examination

# OUTPUT 2: INVALID DATA
# Enter attendance percentage: 65
# Is fee paid? (yes/no): yes
# Is ID card available? (yes/no): yes
# Attendance is insufficient

# EXPLANATION:
# First attendance is checked.
# If attendance is 75 or more, fee payment is checked.
# If fee is paid, ID card is checked.
# Only when all three conditions are satisfied,
# the student can enter the examination.



#! Q3. LIBRARY BOOK ISSUE
#
# QUESTION:
# Input:
# Student membership status
# Account status
# Book availability
#
# Check in order:
# 1. Student is a member.
# 2. Account is active.
# 3. Book is available.
# 4. Issue the book only if all conditions are satisfied.


member = input("Are you a library member? (yes/no): ")
account = input("Is your account active? (yes/no): ")
book = input("Is the book available? (yes/no): ")

if member == "yes":

    if account == "yes":

        if book == "yes":
            print("Book issued successfully")
        else:
            print("Book is not available")

    else:
        print("Account is not active")

else:
    print("Student is not a member")


# OUTPUT 1: VALID DATA
# Are you a library member? (yes/no): yes
# Is your account active? (yes/no): yes
# Is the book available? (yes/no): yes
# Book issued successfully

# OUTPUT 2: INVALID DATA
# Are you a library member? (yes/no): yes
# Is your account active? (yes/no): no
# Is the book available? (yes/no): yes
# Account is not active

# EXPLANATION:
# First membership is checked.
# Then account status is checked.
# Then book availability is checked.
# The book is issued only if all three are yes.



#! Q4. ONLINE SHOPPING CHECKOUT
#
# QUESTION:
# Create a dictionary containing products and prices.
# Ask the user to enter a product.
# Check whether the product exists.
# If it exists, ask for quantity.
# Check whether the quantity is valid.
# Calculate the total amount.
# If the user is a member, apply a discount.
# Display the final amount.
# Do not use loops.


products = {
    "laptop": 50000,
    "phone": 20000,
    "headphone": 2000
}

product = input("Enter product name: ")

if product in products:

    quantity = int(input("Enter quantity: "))

    if quantity > 0:

        total = products[product] * quantity

        member = input("Are you a member? (yes/no): ")

        if member == "yes":

            discount = total * 0.10
            final_amount = total - discount

            print("Total amount:", total)
            print("Discount:", discount)
            print("Final amount:", final_amount)

        else:

            print("Total amount:", total)
            print("Final amount:", total)

    else:
        print("Invalid quantity")

else:
    print("Product not available")


# OUTPUT 1: VALID DATA
# Enter product name: phone
# Enter quantity: 2
# Are you a member? (yes/no): yes
# Total amount: 40000
# Discount: 4000.0
# Final amount: 36000.0

# OUTPUT 2: INVALID DATA
# Enter product name: tablet
# Product not available

# EXPLANATION:
# First we check whether the product exists in the dictionary.
# If it exists, quantity is checked.
# If quantity is valid, total amount is calculated.
# If the customer is a member, 10% discount is applied.



#! Q5. ATM SECURITY
#
# QUESTION:
# Ask for:
# Card inserted status
# PIN correctness
# Account active status
# Withdrawal amount
# Account balance
#
# Allow withdrawal only when:
# 1. Card is inserted.
# 2. PIN is correct.
# 3. Account is active.
# 4. Withdrawal amount is valid.
# 5. Sufficient balance is available.
#
# Display an appropriate message for each failure.


card = input("Is card inserted? (yes/no): ")

if card == "yes":

    pin = input("Is PIN correct? (yes/no): ")

    if pin == "yes":

        account = input("Is account active? (yes/no): ")

        if account == "yes":

            amount = int(input("Enter withdrawal amount: "))

            if amount > 0:

                balance = int(input("Enter account balance: "))

                if amount <= balance:
                    print("Withdrawal successful")
                    print("Remaining balance:", balance - amount)

                else:
                    print("Insufficient balance")

            else:
                print("Invalid withdrawal amount")

        else:
            print("Account is not active")

    else:
        print("Incorrect PIN")

else:
    print("Card is not inserted")


# OUTPUT 1: VALID DATA
# Is card inserted? (yes/no): yes
# Is PIN correct? (yes/no): yes
# Is account active? (yes/no): yes
# Enter withdrawal amount: 5000
# Enter account balance: 20000
# Withdrawal successful
# Remaining balance: 15000

# OUTPUT 2: INVALID DATA
# Is card inserted? (yes/no): yes
# Is PIN correct? (yes/no): no
# Incorrect PIN

# EXPLANATION:
# The conditions are checked one by one.
# Card → PIN → Account → Amount → Balance.
# Withdrawal happens only when all conditions are satisfied.



#! Q6. COLLEGE COURSE REGISTRATION
#
# QUESTION:
# Ask for:
# Login status
# Course name
# Prerequisite completion status
#
# Check in order:
# 1. Student is logged in.
# 2. Selected course exists.
# 3. Prerequisite is completed.
# 4. Allow course registration only if all conditions
#    are satisfied.


logged_in = input("Is student logged in? (yes/no): ")

courses = ["python", "java", "sql"]

if logged_in == "yes":

    course = input("Enter course name: ")

    if course in courses:

        prerequisite = input("Is prerequisite completed? (yes/no): ")

        if prerequisite == "yes":
            print("Course registration successful")
        else:
            print("Prerequisite is not completed")

    else:
        print("Course does not exist")

else:
    print("Student is not logged in")


# OUTPUT 1: VALID DATA
# Is student logged in? (yes/no): yes
# Enter course name: python
# Is prerequisite completed? (yes/no): yes
# Course registration successful

# OUTPUT 2: INVALID DATA
# Is student logged in? (yes/no): yes
# Enter course name: c++
# Course does not exist

# EXPLANATION:
# First login status is checked.
# Then course availability is checked.
# Then prerequisite completion is checked.
# Registration is allowed only when all conditions are satisfied.



#! Q7. JOB APPLICATION
#
# QUESTION:
# Ask for:
# Age
# Qualification
# Years of experience
#
# Check in order:
# 1. Age requirement is satisfied.
# 2. Qualification is valid.
# 3. Required experience is satisfied.
# 4. Display whether the applicant can proceed to the interview.


age = int(input("Enter age: "))

if age >= 18:

    qualification = input("Enter qualification: ")

    if qualification == "degree":

        experience = int(input("Enter years of experience: "))

        if experience >= 1:
            print("Applicant can proceed to the interview")
        else:
            print("Required experience is not satisfied")

    else:
        print("Qualification is not valid")

else:
    print("Age requirement is not satisfied")


# OUTPUT 1: VALID DATA
# Enter age: 25
# Enter qualification: degree
# Enter years of experience: 2
# Applicant can proceed to the interview

# OUTPUT 2: INVALID DATA
# Enter age: 16
# Age requirement is not satisfied

# EXPLANATION:
# First age is checked.
# If age is valid, qualification is checked.
# If qualification is valid, experience is checked.
# If all conditions are satisfied, the applicant can proceed.



#! Q8. HOSPITAL APPOINTMENT
#
# QUESTION:
# Create the dictionary:
#
# doctors = {
#     "doctor1": True,
#     "doctor2": False,
#     "doctor3": True
# }
#
# Ask the patient to enter a doctor name.
# Check whether the doctor exists.
# If the doctor exists, check availability.
# If available, check whether the patient is registered.
# Allow appointment booking only if all conditions are satisfied.


doctors = {
    "doctor1": True,
    "doctor2": False,
    "doctor3": True
}

doctor = input("Enter doctor name: ")

if doctor in doctors:

    if doctors[doctor] == True:

        registered = input("Is patient registered? (yes/no): ")

        if registered == "yes":
            print("Appointment booked successfully")
        else:
            print("Patient is not registered")

    else:
        print("Doctor is not available")

else:
    print("Doctor does not exist")


# OUTPUT 1: VALID DATA
# Enter doctor name: doctor1
# Is patient registered? (yes/no): yes
# Appointment booked successfully

# OUTPUT 2: INVALID DATA
# Enter doctor name: doctor2
# Doctor is not available

# EXPLANATION:
# First we check whether the doctor exists.
# If the doctor exists, availability is checked.
# If the doctor is available, patient registration is checked.
# Appointment is booked only when all conditions are satisfied.



#! Q9. SECURE ROLE-BASED LOGIN
#
# QUESTION:
# Create the dictionary:
#
# users = {
#     "alice": {"password": "1234", "role": "admin"},
#     "bob": {"password": "5678", "role": "student"}
# }
#
# Ask for username and password.
# Check whether the username exists.
# If it exists, check the password.
# If the password is correct, check the user's role.
# Display different access messages for admin and student.
# Handle invalid username and password.


users = {
    "alice": {"password": "1234", "role": "admin"},
    "bob": {"password": "5678", "role": "student"}
}

username = input("Enter username: ")

if username in users:

    password = input("Enter password: ")

    if password == users[username]["password"]:

        if users[username]["role"] == "admin":
            print("Admin access granted")

        elif users[username]["role"] == "student":
            print("Student access granted")

        else:
            print("Unknown role")

    else:
        print("Incorrect password")

else:
    print("Invalid username")


# OUTPUT 1: VALID DATA
# Enter username: alice
# Enter password: 1234
# Admin access granted

# OUTPUT 2: INVALID DATA
# Enter username: bob
# Enter password: 9999
# Incorrect password

# EXPLANATION:
# First username is checked.
# If username exists, password is checked.
# If password is correct, role is checked.
# Admin gets admin access and student gets student access.


# !Q10. FINAL CHALLENGE - COLLEGE STUDENT PORTAL
#
# QUESTION:
# Create a college student portal.
# Ask for username and password.
# Validate login credentials.
# Handle invalid username.
# Handle incorrect password.
#
# After successful login, display:
# 1. View Profile
# 2. Check Attendance
# 3. View Marks
# 4. Course Registration
# 5. Library Access
#
# Handle invalid menu choices.
#
# For Course Registration, check whether prerequisites are completed.
# For Library Access, check membership status.
# For View Marks, check whether marks are available.
#
# Display suitable messages for every situation.
# Use nested conditional statements wherever required.


students = {
    "student1": {
        "password": "1234",
        "prerequisite": True,
        "membership": True,
        "marks": True
    }
}

username = input("Enter username: ")

if username in students:

    password = input("Enter password: ")

    if password == students[username]["password"]:

        print("1. View Profile")
        print("2. Check Attendance")
        print("3. View Marks")
        print("4. Course Registration")
        print("5. Library Access")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Displaying student profile")

        elif choice == 2:
            print("Displaying attendance")

        elif choice == 3:

            if students[username]["marks"] == True:
                print("Displaying marks")
            else:
                print("Marks are not available")

        elif choice == 4:

            if students[username]["prerequisite"] == True:
                print("Course registration available")
            else:
                print("Prerequisites are not completed")

        elif choice == 5:

            if students[username]["membership"] == True:
                print("Library access granted")
            else:
                print("Library membership is not active")

        else:
            print("Invalid menu choice")

    else:
        print("Incorrect password")

else:
    print("Invalid username")


# OUTPUT 1: VALID DATA
# Enter username: student1
# Enter password: 1234
# 1. View Profile
# 2. Check Attendance
# 3. View Marks
# 4. Course Registration
# 5. Library Access
# Enter your choice: 4
# Course registration available


# OUTPUT 2: INVALID DATA
# Enter username: student1
# Enter password: 9999
# Incorrect password

