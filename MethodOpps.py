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

class Student:

    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def Avg_mark(self):

        avg_mark = (self.sub1 + self.sub2 + self.sub3) / 3

        print("\n")
        print(f"Student Name       : {self.name}")
        print(f"Subject 1 Marks    : {self.sub1}")
        print(f"Subject 2 Marks    : {self.sub2}")
        print(f"Subject 3 Marks    : {self.sub3}")
        print(f"Your Average Mark  : {avg_mark}")


s1 = Student("Rahul", 80, 90, 60)
s1.Avg_mark()

            