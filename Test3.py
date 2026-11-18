
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

#Q4 

# class ShoppingCart:
#     def __init__(self, customer_name, product_name, price, quantity):
#         self.customer_name = customer_name
#         self.product_name = product_name
#         self.price = price
#         self.quantity = quantity

#     def calculate_total(self):
#         total = self.price * self.quantity
#         return total

#     @staticmethod
#     def apply_discount(total_amount):
#         if total_amount >= 5000:
#             discount = total_amount * 10 / 100
#             return total_amount - discount
#         else:
#             return total_amount

#     def display_order(self):
#         total = self.calculate_total()
#         final_amount = ShoppingCart.apply_discount(total)

#         print("\n------ SHOPPING ORDER DETAILS ------")
#         print(f"Customer Name: {self.customer_name}")
#         print(f"Product Name: {self.product_name}")
#         print(f"Price: {self.price}")
#         print(f"Quantity: {self.quantity}")
#         print(f"Total Amount: {total}")
#         print(f"Final Amount: {final_amount}")


# s1 = ShoppingCart("Som", "Laptop", 60000, 1)
# s1.display_order()

#Output-->
# ------ SHOPPING ORDER DETAILS ------
# Customer Name: Som
# Product Name: Laptop
# Price: 60000
# Quantity: 1
# Total Amount: 60000
# Final Amount: 54000.0

#Q5

class ElectricityBill:
    def __init__(self, customer_name, meter_name, units_consumed):
        self.customer_name = customer_name
        self.meter_name = meter_name
        self.units_consumed = units_consumed

    @staticmethod
    def validate_units(units):
        return units >= 0

    def calculate_bill(self):
        units = self.units_consumed

        if not ElectricityBill.validate_units(units):
            return "Invalid Units"

        if units <= 100:
            bill = units * 2

        elif units <= 200:
            bill = (100 * 2) + ((units - 100) * 3)

        else:
            bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

        return bill

    def display_bill(self):
        print("\n------ ELECTRICITY BILL ------")
        print(f"Customer Name: {self.customer_name}")
        print(f"Meter Name: {self.meter_name}")
        print(f"Units Consumed: {self.units_consumed}")
        print(f"Total Bill: {self.calculate_bill()}")


e1 = ElectricityBill("Rahul", "MTR101", 250)
e1.display_bill()

#Output-->
# ------ ELECTRICITY BILL ------
# Customer Name: Rahul
# Meter Name: MTR101
# Units Consumed: 250
# Total Bill: 750

        

        