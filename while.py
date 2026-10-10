#!Q1 WAP  to print multiplication table of N number 

n = int (input("Enter the number: "))
i = 1 
while i<=10:
    print (f"{n} x {i} = {n * i}")
    i += 1

#Output =>
# Enter the number: 45
# 45 x 1 = 45
# 45 x 2 = 90
# 45 x 3 = 135
# 45 x 4 = 180
# 45 x 5 = 225
# 45 x 6 = 270
# 45 x 7 = 315
# 45 x 8 = 360
# 45 x 9 = 405
# 45 x 10 = 450

#! Q2 WAP  to print all the even number between the range of 1 to 50

i = 0 
while i<=50:
    if i%2 ==0:
        print (i)
        i+= 1


#! Q3 WAP to print all the chars of user entred string 
s = input ("Enter the string: ")
s = "Python"
i = 0 
while i < len(s):
    char = s[i]
    print(char)
    i+= 1 

#! Q4 WAP to print all the lowercase char from the string 
s = "python"
i= 0 
while i < len (s):
    char = s[i]
    if "a" <= char <= "z":
        print (char)
        i+= 1 

        
#! Q5. WAP to extract all the special characters from a string

s = "Python@123#Hi!"
i = 0

while i < len(s):
    if not s[i].isalnum() and not s[i].isspace():
        print(s[i])
    i += 1

# Output:
# @
# #
# !


#! Q6. WAP to extract all the odd numbers from a given list

L = [30, 15, 2, 40, 37, 28, 76]
i = 0

while i < len(L):
    if L[i] % 2 != 0:
        print(L[i])
    i += 1

# Output:
# 15
# 37
