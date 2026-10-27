
# # Python Conditional Statements - Practice Questions-------------------

# # 1. Print "Positive" if a number is greater than zero.

num =12
if num > 0:
    print ("Positive")



# # 2. Print "Even" if a number is divisible by 2.

num=12
if num % 2 == 0:
    print("Even")

  
# # 3. Print "Eligible to vote" if age is at least 18.

age=20
if age >=18:
    print("Eligible to vote")


# # 4. Check whether a number is even or odd.

num=int(input("Enter a number"))
if num%2==0:
    print("Even")
else:
    print("Odd")


# # 5. Check whether a number is positive or not positive.

num=int(input("Enter a number"))
if num>0:
    print("Positive")
else:
    print("Not positive")


# # 6. Check whether a person is eligible to vote.

age=int(input("Enter Age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



# # 7. Check whether a password matches the correct password.

correct_password="Python@!123"
password= input("Enter Password:")
if password == correct_password:
    print("Login Sucessfully")
else:
    print("Incorrect Password")


# # 8. Check whether a student passes with 40 marks.

mark=int(input("Enter mark:"))
if mark>=40:
    print("Pass")
else:
    print("Fail")


# 9. Print "Negative", "Zero", or "Positive".
num=int(input("Enter a numbe:"))
if num<0:
    print("Invalid Number")
elif num<0:
    print("Negative")
elif num==0:
    print("Zero")
else:
    print("Positive")

# 10. Print grades A, B, C, or Fail.
marks=int(input("Enter Marks:"))
if marks>=80 and marks<=100:
    print("Grade A")
elif marks>=60:
    print("Grade B")
elif marks>=40:
    print("Grade C")
elif marks>0:
    print ("Fail")
else:
    print("Invalid number")

# 11. Classify age as child, teenager, or adult.
age=int(input("Enter age:"))
if age<0:
    print("Invalid Age")
elif age<13:
    print("Child")
elif age<=19:
    print("Teenager")
else:
    print("Adult")

# 12. Make a calculator that handles +, -, *, and /.

# 13. Classify a number as one-digit, two-digit, or three-digit
#     for non-negative inputs below 1000.
