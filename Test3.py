
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

#Q2 
class BankAccount:
    def __init__(self, acc_holder_name, acc_no, balance):
        self.acc_holder_name = acc_holder_name
        self.acc_no = acc_no
        self.balance = balance

    @staticmethod
    def is_valid_amount(amount):
        if amount > 0:
            return True
        else:
            return False

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance = self.balance + amount
            print(f"{amount} Money Deposited Successfully")
        else:
            print(f"Invalid Amount: {amount}")

    def withdraw(self, amount):
        if BankAccount.is_valid_amount(amount):
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(f"{amount} Withdrawn Successfully")
            else:
                print("Insufficient Balance")
        else:
            print(f"Invalid Amount: {amount}")

    def display_balance(self):
        print("\n------ ACCOUNT DETAILS ------")
        print(f"Account Holder: {self.acc_holder_name}")
        print(f"Account Number: {self.acc_no}")
        print(f"Balance: {self.balance}")


b1 = BankAccount("Ram", 1002356, 5000)

b1.display_balance()
b1.deposit(2000)
b1.withdraw(1000)
b1.display_balance()

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

#Q3
  

