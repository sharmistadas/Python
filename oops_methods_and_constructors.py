#! Write a Python program to create a class named
class pyspiders:
    loc = 'KPHB colony'
    branch_head = 'shravani'
    website = "www.pyspiders.com"

# Object 1
s1 = pyspiders()
s1.std_name = "Ashwin"
s1.age = 16
s1.address = "Miyapur"

# Object 2
s2 = pyspiders()
s2.std_name = "Mahesh babu"
s2.age = 19
s2.address = "JNTU"

# Printing class attributes and s1 instance attributes
print(pyspiders.loc, pyspiders.branch_head, pyspiders.website)
print(s1.std_name, s1.age, s1.address)


# Output:
# KPHB colony shravani www.pyspiders.com
# Ashwin 16 Miyapur
# Mahesh babu 19 JNTU



#! Write a Python program to define a class

class pyspiders:
    loc = 'KPHB colony'
    branch_head = 'shravani'
    website = "www.pyspiders.com"

    def disp(self, sid, sname, age, address):
        self.std_id = sid
        self.std_name = sname
        self.std_age = age
        self.std_address = address

# Creating objects
s1 = pyspiders()
s2 = pyspiders()

# Initializing via ClassName.method(object, ...)
pyspiders.disp(s1, 1, 'Ashwin', 20, 'JNTU')
pyspiders.disp(s2, 2, 'Nag Ashwin', 21, 'Uppal')

# Displaying initialized values
print(s1.std_id, s1.std_name, s1.std_age, s1.std_address)
print(s2.std_id, s2.std_name, s2.std_age, s2.std_address)


#Output:

# 1 Ashwin 20 JNTU
# 2 Nag Ashwin 21 Uppal


#!Constructor (_init_)
class pyspiders:
    loc = 'KPHB colony'
    branch_head = 'shravani'
    website = 'www.pyspiders.com'

    # Constructor to initialize object members
    def __init__(self, sid, sname, age, address):
        self.std_id = sid
        self.std_name = sname
        self.std_age = age
        self.std_address = address

# Initializing objects during creation
s1 = pyspiders(1, 'Ashwin', 20, 'JNTU')
s2 = pyspiders(2, 'Nag Ashwin', 21, 'Uppal')

# Printing class attributes
print(pyspiders.loc, pyspiders.branch_head, pyspiders.website)

# Printing object members
print(s1.std_id, s1.std_name, s1.std_age, s1.std_address)
print(s2.std_id, s2.std_name, s2.std_age, s2.std_address)

#Output:
# 1 Ashwin 20 JNTU
# 2 Nag Ashwin 21 Uppal


#! Object Methods (Accessing and Modifying Members)

class pyspiders:
    loc = 'KPHB colony'
    branch_head = 'shravani'
    website = 'www.pyspiders.com'

    def __init__(self, sid, sname, age, address):
        self.std_id = sid
        self.std_name = sname
        self.std_age = age
        self.std_address = address

    # Object method to access object members
    def disp(self):
        print(self.std_id, self.std_name, self.std_age, self.std_address)

    # Object method to modify object members
    def modf_add(self, new_address):
        self.std_address = new_address

# Object creation
s1 = pyspiders(1, 'Ashwin', 20, 'JNTU')

# Displaying class attributes
print(pyspiders.loc, pyspiders.branch_head, pyspiders.website)

# Accessing object members using disp()
s1.disp()

# Modifying address and displaying updated values
s1.modf_add('Ameerpet')
s1.disp()

#Output:
# 1 Ashwin 20 JNTU
# 2 Nag Ashwin 21 Uppal


#! Class Method
class Company:
    cname = "Deloitte"
    ceo = "Ruchita"
    noemp = 1800

    # Constructor
    def __init__(self, eid, ename, sal, desgn):
        self.eid = eid
        self.ename = ename
        self.sal = sal
        self.desgn = desgn

    # Instance method to access object properties
    def disp(self):
        print(self.eid, self.ename, self.sal, self.desgn)

    # Class method to access class properties
    @classmethod
    def display(cls):
        print(cls.cname, cls.ceo, cls.noemp)

    # Class method to modify class property (noemp)
    @classmethod
    def cls_mdf(cls, new_noemp):
        cls.noemp = new_noemp

# Creating an employee object
e1 = Company(1, 'shravya', 80000, 'snr. Python developer')

# Calling methods
e1.disp()
Company.display()

# Modifying class attribute via class method
Company.cls_mdf(2000)
Company.display()
e1.display()

#Output:
# Deloitte Ruchita 1800
# 1 shravya 80000 snr. Python developer
# Deloitte Ruchita 2000
# Deloitte Ruchita 2000


#! Static Method (Simple Utility)

class School:
    sname = "DPS"
    loc = "delhi"

    def __init__(self, sname, marks):
        self.sname = sname
        self.marks = marks

    # Static method used as a helper/supportive method
    @staticmethod
    def result(marks):
        if marks >= 90 and marks <= 100:
            return 'A'
        elif marks >= 75 and marks < 90:
            return 'B'
        elif marks >= 50 and marks < 75:
            return 'C'
        elif marks >= 35 and marks < 50:
            return 'D'
        else:
            return 'Fail'

    # Instance method accessing static helper method
    def disp(self):
        grade = School.result(self.marks)
        print(self.sname, self.marks, grade)

# Driver code
s1 = School("Aman", 95)
s2 = School("Priya", 82)

s1.disp()
s2.disp()


#Output:
# Aman 95 A
# Priya 82 B