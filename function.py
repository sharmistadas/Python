#function without arg without return type

# def add():
#     a=int(input("enter the number: "))
#     b=int(input("enter the number: "))
#     print(a+b)
# add()
# add()    
    
'''
enter the number: 12
enter the number: 23
35
enter the number: 45
enter the number: 34
79

'''

#function with arg without returntype

# def table(a):
#     if type(a)==int:
#         for i in range(1,11):
#             print(f"{a} X {i} ={a*i} ")
# table(26) 

'''
26 X 1 =26 
26 X 2 =52 
26 X 3 =78 
26 X 4 =104 
26 X 5 =130 
26 X 6 =156 
26 X 7 =182 
26 X 8 =208 
26 X 9 =234 
26 X 10 =260 
'''

#fun without arg with returntype

# def div():
#     a=int(input("enter the number: "))
#     b=int(input("enter the number: "))
#     return a/b
# print(div())
# z=div()
# print(z)

'''
enter the number: 10
enter the number: 2
5.0
enter the number: 300
enter the number: 3
100.0
'''


#fun with args with returntype

# def check_bal(acc,pin):
#     acc_num=12345678
#     pin_=1432
#     bal=1000
#     if acc==acc_num:
#         if pin==pin_:
#             return f"Available balance is {bal}"
#         else:
#             return "incorrect pin"
#     else:
#         return "acc not found"
# a=check_bal(12345678,1432)
# print(a)    

'''
Available balance is 1000
'''


#types of Arguments

# 1. POSITIONAL ARG

# def self_intro (name,place,age,parents_name,parents_num):
#     print(f"my name is {name},im from{place},im{age} years old\n  my parents name is {parents_name}\n there contact number is {parents_num}")

# self_intro ("pearl","bidar",22,"praveen",9844704717)  

'''
my name ispearl,im frombidar,im22 years old
  my parents name is praveen
 there contact number is 9844704717
'''

# def self_intro (name,place,age,parents_name,parents_num):
#     print(f"my name is {name}, im from{place}, im{age} years old\n  my parents name is {parents_name}\n there contact number is {parents_num}")

# self_intro (21,"pearl",9844704717,"bidar","praveen")  

'''
my name is 21, im frompearl, im9844704717 years old
  my parents name is bidar
 there contact number is praveen
'''


# 2.KEYWORD ARGS

# def self_intro (name,place,age,parents_name,parents_num):
#     print(f"my name is {name},im from {place}, im {age} years old\n my parents name is {parents_name}\n there contact number is {parents_num}")

# self_intro(parents_num=9876543210 ,age=16,parents_name="Ramaswamy",place="banglore",name="sagar")

'''
my name is sagar,im from banglore, im 16 years old
 my parents name is Ramaswamy
 there contact number is 9876543210
'''