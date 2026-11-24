#hierachical + constructor chaining

class School:
    def _init_(self):
        print("School Name: ABC School")


class Student(School):
    def _init_(self):
        super()._init_()
        print("I am a Student")


class Teacher(School):
    def _init_(self):
        super()._init_()
        print("I am a Teacher")


s = Student()

print("-----")

t = Teacher()

#Hierarchical Inheritance + Constructor Chaining + Method Chaining
class Bank:
    def _init_(self, name):
        self.name = name
        print("Bank Name:", self.name)


class Savings(Bank):
    def _init_(self, name, balance):
        super()._init_(name)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def display(self):
        print("Savings Balance:", self.balance)
        return self


class Current(Bank):
    def _init_(self, name, balance):
        super()._init_(name)
        self.balance = balance

    def display(self):
        print("Current Balance:", self.balance)


s = Savings("SBI", 5000)

s.deposit(1000).display()

print("-----")

c = Current("HDFC", 10000)
c.display()