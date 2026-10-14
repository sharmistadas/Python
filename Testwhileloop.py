#Q! 1-WAP to find the sum of all the int number present in the given tuple 

# t = (10, 20, "Python", 30, 40, 5.5)
# total = 0
# i = 0 
# while i < len(t):
#     chr = t[i]
#     if type(chr) in (int , float):
#        total = total + t[i]
#     i+= 1
# print(total)

# O/P ---- 105.5


#Q! 2-WAP to print all the only the number from the given string 

# s = "HelloPalki234"
# s1 = ""
# i = 0
# while i < len(s):
#     char= s[i]
#     if char.isdigit():
#         s1= s1+char
#     i+=1
# print(s1)

# O/P ---- 234

#Q! 3-WAP to print all the values presented even index from the given list

# l = [10,20,30,40,50,60,70]
# i = 0
# while i < len(l):
#     char = l[i]
#     if i % 2 == 0:
#         print(char)
#     i+=1

# O/P ---- 10 30 50 70

#Q! 4- WAP to create a dict where the keys are uppercase  , lowercase , number , special ch values for the above keys are must be extracted from the user entered string.

# s='pyThon@!123'
# s1={}
# uc  = []
# lc = []
# num = []
# sp = []
# i = 0
# while i<len(s):
#     char  = s[i]
#     if "A"<= char <="Z":
#         uc  += [char]
#     elif "a" <= char <= "z":
#         lc  += [char]
#     elif "0" <= char <= "9":
#         num  += [char]
#     else:
#         sp  += [char]
#     i+=1
# # print(uc,lc,sp,num)
# s1["uppercase"] = uc
# s1["lowercase"] =   lc
# s1["number"] = num 
# s1["specialch"] = sp
# print(s1)

#Q! 5-WAP to find the sum of the asiic values of all the special ch present inside the give string.

# s="ShArmisThA@!1"
# i=0
# sum=0
# while i<len(s):
#     char=s[i]
#     if not(char.isalnum()):
#         sum+=ord(char)
#     i+=1
# print(sum)


#Q! 6-WAP to extarct all the integer numbers prsent inside the given tuple only if the number having more than two digits. 

# t=(15,20,35.5,60,7,9)
# i=0 
# while i<len(t):
#     char=t[i]
#     if len(str(char))==2:
#         print(char)
#     i+=1

#Q! 7- WAP to toggle the given string 

s="HelloHYD"
s1=""
i=0
while i<len(s):
    char=s[i]
    if "A"<= char <= "Z":
        s1+=char.lower()
    elif "a" <= char <= "z":
        s1+=char.upper()
    else :
        s1+= char 
    i+=1
print(s1)

        