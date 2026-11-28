
# =====================================================================
# TOPIC 1: VARIABLES, DATA TYPES & INPUT/OUTPUT
# =====================================================================


# Q1.1 (Billing) A shop sells a pen for 12.5 and a notebook for 45.
#      Store the prices in variables, and print the total cost for
#      3 pens and 2 notebooks in the format: "Total bill: Rs. xxx"


pen_price=12.5
notebook_price=45
total=(3*pen_price+2*notebook_price)
print(f"Total bill: Rs.{total}")

#Output--->
# Total bill: Rs.127.5



# Q1.2 (Profile Card) Take name, age and city as input from the user.
#      Print: "Hi <name>, you are <age> years old and live in <city>."
#      Next year's age should also be printed.


name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
next_year_age=(1+age)
print(f"Hi {name}")
print(f"Your are {age} years old")
print(f"Live in {city}")
print(f"Next year's age: {next_year_age}")

#Output-->
# Hi Rojalin
# Your are 25 years old
# Live in Hyd
# Next year's age: 26


# Q1.3 (Type Check) Create variables of type int, float, str, bool and
#      None. Print each value along with its type using type().

a=100 
b=25.5
c="Sharmistha"
d=True
e=None
print(f"a {type(a)}")
print(f"b {type(b)}")
print(f"c {type(c)}")
print(f"d {type(d)}")
print(f"e {type(e)}")


#Output--->
# a <class 'int'>
# b <class 'float'>
# c <class 'str'>
# d <class 'bool'>
# e <class 'NoneType'>



# Q1.4 (Temperature) Take a temperature in Celsius from the user and
#      convert it to Fahrenheit and Kelvin. Round to 2 decimals.

Celsius=float(input("Enter temperature in Celsius:"))
fahrenheit = (Celsius * 9/5) + 32
kelvin = Celsius + 273.15

print(f"Temperature in Fahrenheit: {round(fahrenheit, 2)} °F")
print(f"Temperature in Kelvin: {round(kelvin, 2)} K")

# output-->
# Enter temperature in Celsius:25
# Temperature in Fahrenheit: 77.0 °F
# Temperature in Kelvin: 298.15 K

# Q1.5 (Swap) You have two cups: tea in cup1 and coffee in cup2.
#      Swap the contents WITHOUT using a third variable (two ways).


cup1 = "Tea"
cup2 = "Coffee"

print("Before Swapping:")
print("Cup 1:", cup1)
print("Cup 2:", cup2)

cup1 = cup1 + cup2
cup2 = cup1.replace(cup2, "")
cup1 = cup1.replace(cup2, "")

print("\nAfter Swapping:")
print("Cup 1:", cup1)
print("Cup 2:", cup2)


#Output-->
# Before Swapping:
# Cup 1: Tea
# Cup 2: Coffee
# After Swapping:
# Cup 1: Coffee
# Cup 2: Tea



# =====================================================================
# TOPIC 2: OPERATORS
# =====================================================================

# Q2.1 (Seconds Converter) Given 10000 seconds, convert to hours,
#      minutes and seconds using // and %.

# Q2.2 (Even/Odd Quick Check) Take a number and print True if it is
#      even, else False, using only operators (no if statement).

# Q2.3 (Discount) A shirt costs 1500 with a 18% discount and then 5%
#      GST on the discounted price. Print the final price.

# Q2.4 (Comparison Chain) Take marks of 3 subjects. Using comparison and
#      logical operators, print True if the student passed all
#      subjects (>= 35 each) AND the average is >= 50.

# Q2.5 (Bitwise Lock) A door lock stores permissions as bits:
#      read=4, write=2, execute=1. Given permission = 6, use bitwise
#      AND to check whether the user has write and execute access.


# =====================================================================
# TOPIC 3: CONDITIONAL STATEMENTS (if / elif / else)
# =====================================================================

# Q3.1 (Grade System) Take marks (0-100). Print grade:
#      90+ A, 75-89 B, 60-74 C, 35-59 D, below 35 Fail.
#      Handle invalid marks (<0 or >100).

# Q3.2 (Movie Ticket) Ticket price: age < 5 free, 5-12 Rs.100,
#      13-59 Rs.200, 60+ Rs.120. Weekend adds Rs.50.
#      Take age and "is_weekend" (yes/no) and print the price.

# Q3.3 (Leap Year) Take a year and tell whether it is a leap year.
#      (Divisible by 4, but not by 100 unless also divisible by 400)

# Q3.4 (ATM Withdrawal) Balance is 5000. Take withdrawal amount.
#      Print "Success" if amount <= balance and multiple of 100,
#      "Insufficient balance" or "Invalid amount" otherwise.

# Q3.5 (Triangle Type) Take 3 sides. First check if a valid triangle
#      is possible, then print equilateral / isosceles / scalene.


# =====================================================================
# TOPIC 4: LOOPS (for / while / break / continue)
# =====================================================================

# Q4.1 (Multiplication Table) Take a number and print its table up to 10
#      in the format: 5 x 3 = 15

# Q4.2 (Digit Sum) Take a number like 4582 and print the sum of its
#      digits using a while loop (no str conversion).

# Q4.3 (Password Attempts) A user has 3 attempts to enter the correct
#      password "python123". Stop on success, lock after 3 failures.

# Q4.4 (Pattern Printing) Print these patterns for n = 5:
#      a) Right triangle of stars
#      b) Inverted triangle of numbers (5 4 3 2 1 / 5 4 3 2 / ...)
#      c) Pyramid of stars

# Q4.5 (Prime Finder) Print all prime numbers between 1 and 100.
#      Use a loop with break. Then count how many there are.


# =====================================================================
# TOPIC 5: STRINGS
# =====================================================================

# Q5.1 (Username Generator) Given full name "  Ravi Kumar Reddy  ",
#      clean spaces, make it lowercase and generate the username
#      "ravi.kumar.reddy".

# Q5.2 (Palindrome) Check whether a given word or sentence is a
#      palindrome ignoring spaces and case. ("Never odd or even")

# Q5.3 (Vowel Counter) Count vowels and consonants in a sentence.
#      Also print the most frequent letter.

# Q5.4 (Email Validator) Check an email: must contain exactly one "@",
#      a "." after the "@", and not start or end with "@" or ".".

# Q5.5 (Caesar Cipher) Encrypt a message by shifting every letter by 3
#      ("abc" -> "def", "xyz" -> "abc"). Keep spaces and symbols as-is.
#      Then write the decrypt version.


# =====================================================================
# TOPIC 6: LISTS
# =====================================================================

# Q6.1 (Shopping Cart) Start with ["milk", "bread", "eggs"]. Add "rice",
#      insert "butter" at position 1, remove "bread", and print the
#      final list and its length.

# Q6.2 (Marks Analysis) marks = [78, 45, 92, 66, 88, 34, 71]
#      Print highest, lowest, average, and the marks sorted in
#      descending order WITHOUT changing the original list.

# Q6.3 (Remove Duplicates) Given [1, 3, 3, 5, 1, 7, 5, 9], remove
#      duplicates while keeping the original order.

# Q6.4 (List Comprehension) From numbers 1-50:
#      a) squares of even numbers
#      b) numbers divisible by both 3 and 5
#      c) list of "Even"/"Odd" labels for 1-10

# Q6.5 (Matrix) Create a 3x3 matrix as a list of lists. Print it nicely,
#      print the sum of each row, each column, and the diagonal.


# =====================================================================
# TOPIC 7: TUPLES & SETS
# =====================================================================

# Q7.1 (Coordinates) Store a point as a tuple (x, y). Unpack it into
#      variables, and write code to find distance between two points.

# Q7.2 (Student Records) students = [("Asha", 82), ("Ravi", 67),
#      ("Meena", 91)]. Sort by marks (highest first) and print the
#      topper's name.

# Q7.3 (Common Friends) Rahul's friends: {"A","B","C","D"},
#      Priya's friends: {"C","D","E","F"}. Find common friends,
#      all friends, only Rahul's friends, and friends exclusive to
#      either (symmetric difference).

# Q7.4 (Unique Visitors) Given a list of 15 website visitor IDs with
#      repeats, find the number of unique visitors and which IDs
#      visited more than once.

# Q7.5 (Anagram Groups) Given ["listen","silent","enlist","google",
#      "gogole","cat","act"], group the anagrams together.
#      (Hint: frozenset or sorted tuple as a key)


# =====================================================================
# TOPIC 8: DICTIONARIES
# =====================================================================

# Q8.1 (Contact Book) Create a dict of 3 contacts (name -> phone).
#      Add one, update one, delete one, and print all in the form
#      "Name: Phone". Safely look up a name that does not exist.

# Q8.2 (Word Frequency) Given a paragraph, count how many times each
#      word appears (ignore case and punctuation). Print the top 3.

# Q8.3 (Inventory) inventory = {"apple": 50, "banana": 20, "mango": 0}
#      a) Print items out of stock
#      b) Reduce "apple" by 15 after a sale
#      c) Print the total number of items in stock

# Q8.4 (Nested Dict) Store 3 students with name, age and a dict of
#      marks {"maths":.., "science":..}. Print each student's total
#      and average, and who scored the highest total.

# Q8.5 (Dict Comprehension) a) Create {n: n**3} for n in 1..10
#      b) Invert {"a":1,"b":2,"c":3} to {1:"a", ...}
#      c) Filter a price dict to items costing more than 100.


# =====================================================================
# TOPIC 9: FUNCTIONS
# =====================================================================

# Q9.1 (Calculator) Write add, subtract, multiply, divide functions.
#      divide should return "Cannot divide by zero" when needed.
#      Make a menu to choose the operation.

# Q9.2 (Default Arguments) Write greet(name, greeting="Hello",
#      punctuation="!"). Call it in 4 different ways (positional,
#      keyword, partial defaults, all values).

# Q9.3 (*args & **kwargs) Write a function that accepts any number of
#      item prices (*args) and optional keyword settings like
#      discount=10, tax=5 (**kwargs), and returns the final bill.

# Q9.4 (Recursion) Write recursive functions for:
#      a) factorial(n)  b) fibonacci(n)  c) sum_of_digits(n)
#      d) power(base, exp)

# Q9.5 (Prime + Return Multiple Values) Write is_prime(n) and a function
#      stats(numbers) that returns min, max and average together.
#      Use is_prime to filter primes from a list.


# =====================================================================
# TOPIC 10: LAMBDA, MAP, FILTER, SORTED, ZIP
# =====================================================================

# Q10.1 (Price Increase) Use map + lambda to add 10% GST to a list of
#       prices [100, 250, 399, 50].

# Q10.2 (Adults Only) Use filter + lambda to keep people aged 18+ from
#       a list of dicts [{"name":"A","age":17}, ...].

# Q10.3 (Sort Employees) Sort a list of employee tuples
#       (name, salary, age) by salary descending, then by name
#       using sorted() with a key lambda.

# Q10.4 (Zip Report) names = [...], marks = [...], city = [...].
#       Use zip to print one line per student, then build a dict of
#       name -> marks using zip.

# Q10.5 (Enumerate & Reduce) Print a numbered to-do list starting at 1
#       using enumerate. Then use functools.reduce to find the product
#       of [1, 2, 3, 4, 5].


# =====================================================================
# TOPIC 11: FILE HANDLING
# =====================================================================

# Q11.1 (Notes App) Ask the user for a note and append it with a
#       timestamp to notes.txt. Then read and display all notes.

# Q11.2 (Line Counter) Read a text file and print number of lines,
#       words and characters (like the wc command).

# Q11.3 (CSV Marks) Create students.csv (name,marks). Read it with the
#       csv module and print the names of those who scored above the
#       class average.

# Q11.4 (Find & Replace) Read a file, replace every occurrence of a
#       word with another word, and save to a new file.

# Q11.5 (JSON Settings) Save a dict of app settings to settings.json,
#       load it back, change one value, and save again.


# =====================================================================
# TOPIC 12: EXCEPTION HANDLING
# =====================================================================

# Q12.1 (Safe Input) Keep asking for an integer until the user enters a
#       valid one. Use try/except ValueError.

# Q12.2 (Safe Division) Take two numbers and divide them. Handle
#       ZeroDivisionError and ValueError separately, and print
#       "Done" using finally.

# Q12.3 (File Not Found) Try to open a file name given by the user.
#       If missing, print a friendly message and create it.

# Q12.4 (Custom Exception) Create InsufficientBalanceError. Write
#       withdraw(balance, amount) that raises it when needed.
#       Catch it and print a helpful message.

# Q12.5 (Retry Logic) Simulate a flaky network call (random failure).
#       Retry up to 3 times with try/except, printing each attempt.


# =====================================================================
# TOPIC 13: MODULES & STANDARD LIBRARY
# =====================================================================

# Q13.1 (Dice Game) Use random to roll two dice until you get a double.
#       Print how many rolls it took.

# Q13.2 (Age Calculator) Use datetime to take a birth date and print
#       exact age in years, months and days, plus days until the
#       next birthday.

# Q13.3 (Own Module) Create mymath.py with 3 functions (square, cube,
#       is_even). Import it in another file in 3 different ways.

# Q13.4 (Math & Stats) Use math and statistics modules to compute the
#       square root, ceiling, floor, GCD of two numbers, and the mean,
#       median and mode of a list.

# Q13.5 (Password Generator) Use random and string to generate a
#       strong 12-character password with at least one uppercase,
#       lowercase, digit and symbol.


# =====================================================================
# TOPIC 14: OOP - CLASSES & OBJECTS
# =====================================================================

# Q14.1 (Student Class) Create class Student with name, roll_no and
#       marks attributes and a method display(). Create 3 objects.

# Q14.2 (Rectangle) Create class Rectangle(length, width) with methods
#       area(), perimeter() and is_square(). Test with 3 objects.

# Q14.3 (Counter) Create class Counter with methods increment(),
#       decrement(), reset() and a value that never goes below 0.

# Q14.4 (Class vs Instance Variables) Create class Employee with a
#       class variable company_name and instance variables name and
#       salary. Add a class variable that counts total employees.

# Q14.5 (Library Book) Create class Book(title, author, is_available).
#       Add methods borrow() and return_book() that update the status
#       and print proper messages (e.g. already borrowed).


# =====================================================================
# TOPIC 15: OOP - CONSTRUCTORS, ENCAPSULATION & PROPERTIES
# =====================================================================

# Q15.1 (Bank Account) Create BankAccount with a private __balance.
#       Provide deposit(), withdraw() (no overdraft) and get_balance().
#       Show that direct access to __balance fails.

# Q15.2 (Property Decorators) Create class Person with age as a
#       @property. The setter should reject negative or > 120 values.

# Q15.3 (Temperature Class) Class Temperature stores Celsius privately.
#       Add a fahrenheit property with both getter and setter.

# Q15.4 (Class & Static Methods) In class Pizza, add a @classmethod
#       margherita() and a @classmethod pepperoni() that return
#       pre-configured pizzas, and a @staticmethod is_valid_size(size).

# Q15.5 (ATM PIN) Create class ATMCard with a private PIN. Let the
#       user change the PIN only if the old PIN is correct, and lock
#       the card after 3 wrong attempts.


# =====================================================================
# TOPIC 16: OOP - INHERITANCE
# =====================================================================

# Q16.1 (Vehicles) Base class Vehicle(brand, speed) with start().
#       Child classes Car and Bike add their own attributes and
#       override start() with a different message.

# Q16.2 (Employees) Base class Employee(name, salary). Subclasses
#       Manager (adds bonus) and Developer (adds language). Use
#       super().__init__ and override calculate_pay().

# Q16.3 (Multilevel) Create Animal -> Mammal -> Dog. Each level adds
#       one attribute and one method. Call all methods on a Dog.

# Q16.4 (Multiple Inheritance) Create classes Flyer (fly) and Swimmer
#       (swim). Create Duck(Flyer, Swimmer). Print Duck.__mro__ and
#       explain the order.

# Q16.5 (School System) Person -> Student and Person -> Teacher.
#       Student has grades, Teacher has subjects. Add a School class
#       that stores both and prints a full report (composition).


# =====================================================================
# TOPIC 17: OOP - POLYMORPHISM & MAGIC (DUNDER) METHODS
# =====================================================================

# Q17.1 (Shapes) Classes Circle, Square, Triangle each with area().
#       Put them in one list and loop to print the area of each
#       without checking types.

# Q17.2 (Payment Methods) Classes CreditCard, UPI and Cash with a
#       pay(amount) method behaving differently. Write a checkout()
#       function that accepts any of them.

# Q17.3 (__str__ and __repr__) Make a Product class that prints nicely
#       with print() and shows a developer-friendly form in a list.

# Q17.4 (Operator Overloading) Create class Vector(x, y) supporting
#       v1 + v2, v1 - v2, v1 * 3, v1 == v2 and abs(v1).

# Q17.5 (Container Protocol) Create class Playlist that supports
#       len(p), p[0], "song" in p, for song in p, and p += "new song"
#       using __len__, __getitem__, __contains__, __iter__, __iadd__.


# =====================================================================
# TOPIC 18: OOP - ABSTRACTION & ADVANCED CONCEPTS
# =====================================================================

# Q18.1 (Abstract Base Class) Create abstract class Shape (abc module)
#       with abstract methods area() and perimeter(). Show that you
#       cannot instantiate Shape, then implement Circle and Rectangle.

# Q18.2 (Notification System) Abstract class Notifier with send().
#       Implement EmailNotifier, SMSNotifier, PushNotifier.
#       Write a function that sends one message through all of them.

# Q18.3 (Dataclass) Rewrite a Student class using @dataclass with
#       default values, ordering by marks, and a frozen version.

# Q18.4 (Singleton) Create a Logger class where only ONE instance can
#       ever exist, no matter how many times you create it.
#       Prove it with the `is` operator.

# Q18.5 (Composition) Build a Car class that HAS an Engine, 4 Wheels
#       and a MusicSystem object. Delegate car.start() to
#       engine.start() and explain why this is better than
#       inheriting from Engine.


# =====================================================================
# FINAL MINI PROJECTS (Combine everything!)
# =====================================================================

# P1. (Library Management System) Classes: Book, Member, Library.
#     Features: add/remove books, issue/return, due date with
#     datetime, late fines, save/load data using JSON, custom
#     exceptions for errors.

# P2. (Bank System) Abstract Account -> Savings, Current. Transaction
#     history, interest calculation, file persistence, menu-driven CLI.

# P3. (Student Result Manager) Read marks from CSV, compute grades,
#     rank students, write a report file, handle bad data gracefully.

# P4. (Inventory/Billing App) Product class, Cart class, discounts via
#     polymorphism, invoice printed in a neat formatted table.

# P5. (Text Adventure Game) Player, Room and Item classes, inventory
#     dictionary, game loop, save/load game state.