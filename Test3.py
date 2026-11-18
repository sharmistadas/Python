
# # Q1: 

# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def display_details(self):
#         result = Student.check_result(self.marks)

#         print(f"\nStudent Name: {self.name}")
#         print(f"Roll Number: {self.roll_number}")
#         print(f"Marks: {self.marks}")
#         print(f"Result: {result}")

#     @staticmethod
#     def check_result(marks):
#         return "Pass" if marks >= 35 else "Fail"


# s1 = Student("Bibhu", 101, 78)
# s2 = Student("Bharti", 102, 35)
# s3 = Student("Roma", 108, 87)

# students = [s1, s2, s3]

# for student in students:
#     student.display_details()


#Output-->

# Student Name: Bibhu
# Roll Number: 101
# Marks: 78
# Result: Pass

# Student Name: Bharti
# Roll Number: 102
# Marks: 35
# Result: Pass

# Student Name: Roma
# Roll Number: 108
# Marks: 87
# Result: Pass

# #Q2 
# class BankAccount:
#     def __init__(self, acc_holder_name, acc_no, balance):
#         self.acc_holder_name = acc_holder_name
#         self.acc_no = acc_no
#         self.balance = balance

#     @staticmethod
#     def is_valid_amount(amount):
#         if amount > 0:
#             return True
#         else:
#             return False

#     def deposit(self, amount):
#         if BankAccount.is_valid_amount(amount):
#             self.balance = self.balance + amount
#             print(f"{amount} Money Deposited Successfully")
#         else:
#             print(f"Invalid Amount: {amount}")

#     def withdraw(self, amount):
#         if BankAccount.is_valid_amount(amount):
#             if amount <= self.balance:
#                 self.balance = self.balance - amount
#                 print(f"{amount} Withdrawn Successfully")
#             else:
#                 print("Insufficient Balance")
#         else:
#             print(f"Invalid Amount: {amount}")

#     def display_balance(self):
#         print("\n------ ACCOUNT DETAILS ------")
#         print(f"Account Holder: {self.acc_holder_name}")
#         print(f"Account Number: {self.acc_no}")
#         print(f"Balance: {self.balance}")


# b1 = BankAccount("Ram", 1002356, 5000)

# b1.display_balance()
# b1.deposit(2000)
# b1.withdraw(1000)
# b1.display_balance()

#Output-->
# ------ ACCOUNT DETAILS ------
# Account Holder: Ram
# Account Number: 1002356
# Balance: 5000
# 2000 Money Deposited Successfully
# 1000 Withdrawn Successfully

# ------ ACCOUNT DETAILS ------
# Account Holder: Ram
# Account Number: 1002356
# Balance: 6000

# #Q3

# class Employee:
#     def __init__(self, employee_name, employee_id, basic_salary):
#         self.employee_name = employee_name
#         self.employee_id = employee_id
#         self.basic_salary = basic_salary

#     @staticmethod
#     def is_valid_salary(salary):
#         return salary > 0

#     def calculate_sal(self):
#         if Employee.is_valid_salary(self.basic_salary):
#             hra = self.basic_salary * 20 / 100
#             da = self.basic_salary * 10 / 100

#             final_salary = self.basic_salary + hra + da
#             return final_salary
#         else:
#             return "Invalid Salary"

#     def display_details(self):
#         print("\n------ EMPLOYEE DETAILS ------")
#         print(f"Employee Name: {self.employee_name}")
#         print(f"Employee ID: {self.employee_id}")
#         print(f"Basic Salary: {self.basic_salary}")
#         print(f"Final Salary: {self.calculate_sal()}")


# e1 = Employee("Soraj", 101, 30000)
# e1.display_details()

#Output-->
# ------ EMPLOYEE DETAILS ------
# Employee Name: Soraj
# Employee ID: 101
# Basic Salary: 30000
# Final Salary: 39000.0
