
# Q1: 

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        result = Student.check_result(self.marks)

        print(f"\nStudent Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Result: {result}")

    @staticmethod
    def check_result(marks):
        return "Pass" if marks >= 35 else "Fail"


s1 = Student("Bibhu", 101, 78)
s2 = Student("Bharti", 102, 35)
s3 = Student("Roma", 108, 87)

students = [s1, s2, s3]

for student in students:
    student.display_details()


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
