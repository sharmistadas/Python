# #Q1Write a Python program to create a class High_Alert with a method smoke_alert() that performs the


# class High_Alert:

#     def smoke_alert(self):

#         cities = ["Delhi", "Hyd", "Chennai", "Bbsr", "Mumbai"]

#         high_alert_cities = {city.upper() for city in cities}

#         city = input("Enter your city name: ").upper()

#         if city in high_alert_cities:
#             print(f"{city} is in a red zone with high smoke and pollution.")
#         else:
#             print(f"{city} is not listed as a high-alert city.")


# h = High_Alert()
# h.smoke_alert()



# #Q2 Calculate Employee In-Hand Salary Using a Class and Method


# class Emp:

#     def in_hand_sal(self, name, ctc, role, id):

#         gst = 18
#         pf = 1800
#         insurance = 350
#         cab = 1400

#         tax_amt = ctc * gst / 100
#         total_pf = pf * 12
#         total_insurance = insurance * 12
#         yearly_cab = cab * 12

#         total_deductions = (
#             tax_amt + total_pf + total_insurance + yearly_cab
#         )

#         in_hand_salary = ctc - total_deductions

#         print("\n---------- EMPLOYEE DETAILS ----------")
#         print(f"Employee ID       : {id}")
#         print(f"Employee Name     : {name}")
#         print(f"Employee Role     : {role}")
#         print(f"Yearly CTC        : ₹{ctc}")
#         print(f"Tax (18%)         : ₹{tax_amt}")
#         print(f"Yearly PF         : ₹{total_pf}")
#         print(f"Yearly Insurance  : ₹{total_insurance}")
#         print(f"Yearly Cab        : ₹{yearly_cab}")
#         print(f"Total Deductions  : ₹{total_deductions}")
#         print(f"In-Hand Salary    : ₹{in_hand_salary}")


# e = Emp()
# e.in_hand_sal("Rahul", 600000, "Python Developer", 101)



#Q3  Create a Student class that takes name and marks of 3 subjects as arguments in the constructor. 
# Then create amethod to print the average

# class Student:

#     def __init__(self, name, sub1, sub2, sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3

#     def Avg_mark(self):

#         avg_mark = (self.sub1 + self.sub2 + self.sub3) / 3

#         print("\n")
#         print(f"Student Name       : {self.name}")
#         print(f"Subject 1 Marks    : {self.sub1}")
#         print(f"Subject 2 Marks    : {self.sub2}")
#         print(f"Subject 3 Marks    : {self.sub3}")
#         print(f"Your Average Mark  : {avg_mark}")


# s1 = Student("Rahul", 80, 90, 60)
# s1.Avg_mark()

#Q4 Student Class
# Create a Student class that accepts the following details in the constructor:
# - Student name
# - Roll number
# - Marks of 3 subjects
# Create a method display() to print all student details.


# class Student:
#     def __init__(self, name, rollno, sub1, sub2, sub3):
#         self.name = name
#         self.rollno = rollno
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3

#     def display(self):
#         print("\n------Student Details------")
#         print(f"Student Name: {self.name}")
#         print(f"Roll No: {self.rollno}")
#         print(f"Subject 1 marks: {self.sub1}")
#         print(f"Subject 2 marks: {self.sub2}")
#         print(f"Subject 3 marks: {self.sub3}")



# S1 = Student("Rahul", 101, 80, 70, 60)


# S1.display()

#Q5 Employee Class
# Create an Employee class that accepts the following details in the constructor:
# - Employee name
# - Employee ID
# - Employee salary
# Create a method display() to print all employee details.

# class Employee:
#     def __init__ (self, emp_name, emp_id, emp_sal):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.emp_sal = emp_sal

#     def display(self):
#         print("\n----- All Employee Details -----")
#         print(f"EMP Name   : {self.emp_name}")
#         print(f"EMP ID     : {self.emp_id}")
#         print(f"EMP Salary : {self.emp_sal}")


# e1 = Employee("Raju", 201, 5000)
# e1.display()

#Q6 Create a Rectangle class that accepts length and breadth as arguments in the constructor.
# Create two methods:
# - area() – Calculate and print the area.
# - perimeter() – Calculate and print the perimeter.

# class Rectangle:
#     def __init__ (self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         calculated_area = self.length * self.breadth
#         print(f"Area      : {calculated_area}")

#     def perimeter(self):
#         calculated_perimeter = 2 * (self.length + self.breadth)
#         print(f"Perimeter : {calculated_perimeter}")

# r = Rectangle(50, 30)
# r.area()
# r.perimeter()


#Q7 Create a BankAccount class that accepts the following details in the constructor:
# - Account holder name
# - Account number
# - Initial balance
# Create two methods:
# - deposit() – Add an amount to the existing balance and print the updated balance.
# - display() – Print account holder name, account number and balance.



class BankAccount:
    def __init__ (self, acc_holder_name, acc_no, initial_balance):
        self.acc_holder_name = acc_holder_name
        self.acc_no = acc_no
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Updated Balance: {self.balance}")

    def display(self):
        print("\n--- Account Details ---")
        print(f"Account Holder Name : {self.acc_holder_name}")
        print(f"Account Number      : {self.acc_no}")
        print(f"Account Balance     : {self.balance}")


account = BankAccount("Rahul Sharma" , "123456789", 5000)
account.display()
account.deposit(2000)
            