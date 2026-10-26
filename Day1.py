
# Python Conditional Statements - Practice Questions-------------------

# 1. Print "Positive" if a number is greater than zero.

num =12
if num > 0:
    print ("Positive")



# 2. Print "Even" if a number is divisible by 2.

num=12
if num % 2 == 0:
    print("Even")

  
# 3. Print "Eligible to vote" if age is at least 18.

age=20
if age >=18:
    print("Eligible to vote")


# 4. Check whether a number is even or odd.

num=int(input("Enter a number"))
if num%2==0:
    print("Even")
else:
    print("Odd")



# 5. Check whether a number is positive or not positive.

num=int(input("Enter a number"))
if num>0:
    print("Positive")
else:
    print("Not positive")


# 6. Check whether a person is eligible to vote.

age=int(input("Enter Age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



# 7. Check whether a password matches the correct password.

correct_password="Python@!123"
password= input("Enter Password:")
if password == correct_password:
    print("Login Sucessfully")
else:
    print("Incorrect Password")


# 8. Check whether a student passes with 40 marks.

mark=int(input("Enter mark:"))
if mark>=40:
    print("Pass")
else:
    print("Fail")