
# ==================================================
#        PYTHON OOP - VEHICLE RENTAL SYSTEM
# ==================================================

# QUESTION:

# Write a Python program to develop a Vehicle Rental
# Management System using Object-Oriented Programming.

# REQUIREMENTS:

# 1. DECORATOR:
#    - Create a decorator named rental_info().
#    - Display "Calculating rental amount..." whenever
#      the rental amount is calculated.

# 2. PARENT CLASS - Vehicle:
#    - Create a class named Vehicle.
#    - Create a constructor to initialize:
#        vehicle_number
#        model
#        price_per_day
#    - Use private variables for encapsulation.
#    - Create an instance method calculate_rent(days).
#    - Create a static method valid_days(days).
#    - Create getter methods for all private variables.

# 3. CHILD CLASS - Car:
#    - Inherit the Vehicle class.
#    - Override calculate_rent(days).
#    - Add an extra charge of Rs.200 per day.
#    - Use super() to call the parent method.

# 4. CHILD CLASS - Bike:
#    - Inherit the Vehicle class.
#    - Override calculate_rent(days).
#    - Add an extra charge of Rs.50 per day.
#    - Use super() to call the parent method.

# 5. OBJECT CREATION:

#    Create the following objects:

#    Car:
#    1. CAR101, Swift, 1500
#    2. CAR102, Hyundai, 1200

#    Bike:
#    3. BIKE101, Honda, 500
#    4. BIKE102, Yamaha, 800

# 6. LIST:
#    - Store all vehicle objects in a list named
#      rented_vehicles.

# 7. USER INPUT:
#    - Take rental days from the user.
#    - Convert input into an integer.
#    - Validate rental days using valid_days().

# 8. FOR LOOP:
#    - Iterate through the vehicle list.
#    - Display vehicle number, model and price per day.
#    - Calculate and display total rental amount.

# 9. CONDITIONAL STATEMENT:
#    - Display vehicles whose price per day is
#      greater than Rs.1000.
#    - Use the greater than (>) operator.

# 10. EXCEPTION HANDLING:
#     - Use try-except.
#     - Handle ValueError.
#     - Display an error message for invalid input.
#     - Display an error message if days are zero
#       or negative.

# ==================================================
#                  EXPECTED OUTPUT
# ==================================================

# Enter rental days: 3

# ----- Vehicle Rental Details -----

# Vehicle Number: CAR101
# Model: Swift
# Price Per Day: Rs.1500
# Total Rent: Rs.5100

# Vehicle Number: CAR102
# Model: Hyundai
# Price Per Day: Rs.1200
# Total Rent: Rs.4200

# Vehicle Number: BIKE101
# Model: Honda
# Price Per Day: Rs.500
# Total Rent: Rs.1650

# Vehicle Number: BIKE102
# Model: Yamaha
# Price Per Day: Rs.800
# Total Rent: Rs.2550

# Vehicles with price greater than Rs.1000:
# Swift
# Hyundai

# ==================================================
#                  PRACTICE TASK
# ==================================================

# Write the complete program independently.

# Do not copy the previous answer.

# Concepts to remember:
# - Class and Object
# - Constructor
# - Inheritance
# - Method Overriding
# - super()
# - Encapsulation
# - Getter Methods
# - Static Method
# - Decorator
# - List
# - For Loop
# - If-Else
# - Exception Handling
# - f-String
# ==================================================



# Decorator
def rental_info(func):
    def wrapper(*args, **kwargs):
        print("Calculating rental amount...")
        return func(*args, **kwargs)
    return wrapper


# Parent Class
class Vehicle:

    def __init__(self, vehicle_number, model, price_per_day):
        self.__vehicle_number = vehicle_number
        self.__model = model
        self.__price_per_day = price_per_day

    # Instance Method
    @rental_info
    def calculate_rent(self, days):
        return self.__price_per_day * days

    # Static Method
    @staticmethod
    def valid_days(days):
        return days > 0

    # Getter Methods (Encapsulation)
    def get_vehicle_number(self):
        return self.__vehicle_number

    def get_model(self):
        return self.__model

    def get_price_per_day(self):
        return self.__price_per_day


# Child Class - Car
class Car(Vehicle):

    @rental_info
    def calculate_rent(self, days):
        return super().calculate_rent(days) + (200 * days)


# Child Class - Bike
class Bike(Vehicle):

    @rental_info
    def calculate_rent(self, days):
        return super().calculate_rent(days) + (50 * days)


# Creating Objects
car1 = Car("CAR101", "Swift", 1500)
car2 = Car("CAR102", "Hyundai", 1200)

bike1 = Bike("BIKE101", "Honda", 500)
bike2 = Bike("BIKE102", "Yamaha", 800)


# Storing Objects in a List
rented_vehicles = [car1, car2, bike1, bike2]


# Taking Input
try:
    days = int(input("Enter rental days: "))

    if Vehicle.valid_days(days):

        print("\n----- Vehicle Rental Details -----")

        # For Loop
        for vehicle in rented_vehicles:

            print(f"\nVehicle Number: {vehicle.get_vehicle_number()}")
            print(f"Model: {vehicle.get_model()}")
            print(f"Price Per Day: ₹{vehicle.get_price_per_day()}")

            total = vehicle.calculate_rent(days)

            print(f"Total Rent: ₹{total}")

        # Using Greater Than (>) Operator
        print("\nVehicles with price greater than ₹1000:")

        for vehicle in rented_vehicles:
            if vehicle.get_price_per_day() > 1000:
                print(f"{vehicle.get_model()}")

    else:
        print("Error: Rental days must be greater than 0.")

except ValueError:
    print("Error: Please enter a valid number.")


#Output --->
# Enter rental days: 3

# ----- Vehicle Rental Details -----

# Vehicle Number: CAR101
# Model: Swift
# Price Per Day: ₹1500
# Calculating rental amount...
# Calculating rental amount...
# Total Rent: ₹5100

# Vehicle Number: CAR102
# Model: Hyundai
# Price Per Day: ₹1200
# Calculating rental amount...
# Calculating rental amount...
# Total Rent: ₹4200

# Vehicle Number: BIKE101
# Model: Honda
# Price Per Day: ₹500
# Calculating rental amount...
# Calculating rental amount...
# Total Rent: ₹1650

# Vehicle Number: BIKE102
# Model: Yamaha
# Price Per Day: ₹800
# Calculating rental amount...
# Calculating rental amount...
# Total Rent: ₹2550

# Vehicles with price greater than ₹1000:
# Swift
# Hyundai