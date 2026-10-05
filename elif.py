# ! WAP to check weather  ch is uppercase lowercae digit or special ch ?

ch = input("enter the ch : ")
if ch.isupper():
    print ("uppercase")

elif ch.islower():
    print ("lowercase")


elif ch.isdigit():
    print ("number")

else:
    print ("special ch")


#! WAP  to check weather what type of dat user entered ?

data = eval(input("enter the data : "))
if type(data) == int:
    print ("interger")

elif type(data) == float:
    print ("float")

elif type(data) == complex:
    print ("complex")

elif type(data) == bool:
    print ("boolean")

elif type(data) == str:
    print ("string")

elif type(data) == list:
    print ("list")

elif type(data) == tuple:
    print ("tuple")

elif type(data) == set:
    print ("set")

elif type(data) == dict:
    print ("dict")

else:
    print("nothing")


#! WAP  to take 6 input from user as the marks of each subject and calculate the average and display the grade 

m1 = int(input("Enter the marks of subject 1: "))
m2 = int(input("Enter the marks of subject 2: "))
m3 = int(input("Enter the marks of subject 3: "))
m4 = int(input("Enter the marks of subject 4: "))
m5 = int(input("Enter the marks of subject 5: "))
m6 = int(input("Enter the marks of subject 6: "))

average = (m1 + m2 + m3 + m4 + m5 + m6) / 6

print("Average marks:", average)

if average >= 90:
    print("Grade A")

elif average >= 80:
    print("Grade B")

elif average >= 70:
    print("Grade C")

elif average >= 60:
    print("Grade D")

elif average >= 50:
    print("Grade E")

else:
    print("Grade F")


#! wap to check greatest of 3 number 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print("First number is greatest")

elif num2 > num1 and num2 > num3:
    print("Second number is greatest")

elif num3 > num1 and num3 > num2:
    print("Third number is greatest")

else:
    print("Some numbers are equal")
