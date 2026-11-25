
# Q1. Employee Salary (Inheritance)
# Create a parent class Employee and a child class PermanentEmployee.
# - Employee has name and basic salary.
# - PermanentEmployee has an additional bonus.
# - Calculate and display the total salary.

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

class PermanentEmployee(Employee):
    def __init__(self, name, basic_salary, bonus):
        super().__init__(name, basic_salary)
        self.bonus = bonus

    def total_salary(self):
        return self.basic_salary + self.bonus

e = PermanentEmployee("Ravi", 30000, 5000)
print("Q1:", e.name, "Total Salary:", e.total_salary())

# Output:
# Q1: Ravi Total Salary: 35000


# Q2. Product Details (Inheritance)
# Create a parent class Product and a child class Mobile.
# - Product has product name and price.
# - Mobile has an additional warranty period.
# - Display all product details.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Mobile(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display(self):
        print("Q2:", self.name, self.price, self.warranty, "years")

m = Mobile("Samsung", 20000, 2)
m.display()

# Output:
# Q2: Samsung 20000 2 years


# Q3. Payment System (Polymorphism)
# Create two classes CashPayment and CardPayment.
# - Both classes must have a pay() method.
# - Cash payment and card payment should have different implementations.
# - Create objects and demonstrate polymorphism.

class CashPayment:
    def pay(self, amount):
        print("Q3: Cash payment:", amount)

class CardPayment:
    def pay(self, amount):
        print("Q3: Card payment:", amount)

for payment in (CashPayment(), CardPayment()):
    payment.pay(1000)

# Output:
# Q3: Cash payment: 1000
# Q3: Card payment: 1000


# Q4. Area of Shapes (Polymorphism)
# Create two classes Rectangle and Circle.
# - Rectangle requires length and breadth.
# - Circle requires radius.
# - Both classes must have a calculate_area() method.
# - Display the area of each shape.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

for shape in (Rectangle(10, 5), Circle(7)):
    print("Q4: Area:", round(shape.calculate_area(), 2))

# Output:
# Q4: Area: 50
# Q4: Area: 153.86


# Q5. Bank Account (Encapsulation)
# Create a class BankAccount.
# - Create a private attribute balance.
# - Use the @property decorator to read the balance.
# - Create a setter that rejects negative values.
# - Include deposit and withdrawal methods.
# - Display the updated balance.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid balance")

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Invalid withdrawal")

b = BankAccount(5000)
b.deposit(1000)
b.withdraw(2000)
print("Q5: Balance:", b.balance)

# Output:
# Q5: Balance: 4000


# Q6. Student Marks (Encapsulation)
# Create a class Student.
# - Create a private attribute marks.
# - Use a property getter and setter.
# - Marks must be between 0 and 100.
# - Invalid marks should not update the existing marks.
# - Display the student's marks.

class Student:
    def __init__(self, marks):
        self.__marks = 0
        self.marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")

s = Student(85)
s.marks = 120
print("Q6: Marks:", s.marks)

# Output:
# Invalid marks
# Q6: Marks: 85


# Q7. Employee Attendance (Abstraction)
# Create an abstract class Employee.
# - Declare an abstract method mark_attendance().
# - Create child classes OfficeEmployee and RemoteEmployee.
# - Implement the attendance method differently in each child class.
# - Display the attendance details.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def mark_attendance(self):
        pass

class OfficeEmployee(Employee):
    def mark_attendance(self):
        print("Q7: Office attendance marked")

class RemoteEmployee(Employee):
    def mark_attendance(self):
        print("Q7: Online attendance marked")

OfficeEmployee().mark_attendance()
RemoteEmployee().mark_attendance()

# Output:
# Q7: Office attendance marked
# Q7: Online attendance marked


# Q8. Uber Ride Fare (Inheritance + Constructor Chaining)
# Create a parent class Ride and child classes BikeRide and CarRide.
# - Ride has passenger name and distance travelled.
# - BikeRide fare is ₹10 per kilometre.
# - CarRide fare is ₹20 per kilometre.
# - Use constructor chaining with super() to initialize passenger name and distance.
# - Calculate and display the fare for each ride.
    
class Ride:
    def __init__(self, passenger, distance):
        self.passenger = passenger
        self.distance = distance

class BikeRide(Ride):
    def __init__(self, passenger, distance):
        super().__init__(passenger, distance)

    def fare(self):
        return self.distance * 10

class CarRide(Ride):
    def __init__(self, passenger, distance):
        super().__init__(passenger, distance)

    def fare(self):
        return self.distance * 20

bike = BikeRide("Amit", 5)
car = CarRide("Priya", 5)

print("Q8:", bike.passenger, "Bike Fare:", bike.fare())
print("Q8:", car.passenger, "Car Fare:", car.fare())

# Output:
# Q8: Amit Bike Fare: 50
# Q8: Priya Car Fare: 100
