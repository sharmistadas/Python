# Scenario:
# An e-commerce platform receives thousands of orders every minute. 
# To reduce memory usage, orders should be processed one at a time.

# Question:
# Given a list of orders, write a generator that yields one order at a time. 
# Then write code to process each order as it is received.

# Q1. WAGP which yields even numbers from 50 to 70.
# WAGP = Write A Generator Program

# ANSWER:

def even_numbers():
    for i in range(50, 71):
        if i % 2 == 0:
            yield i

for num in even_numbers():
    print(num, end=" ")

# OUTPUT:
# 50 52 54 56 58 60 62 64 66 68 70

# EXPLANATION:
# range(50, 71) generates numbers from 50 to 70.
# % 2 == 0 checks whether a number is even.
# yield returns each even number one at a time.


# ============================================================
# Q2. WAGF to yield only float values from a list.
# WAGF = Write A Generator Function
# ============================================================

# ANSWER:

def float_values(data):
    for value in data:
        if isinstance(value, float):
            yield value

numbers = [10, 20.5, 30, 40.8, 50, 60.5, "Python"]

for num in float_values(numbers):
    print(num)

# OUTPUT:
# 20.5
# 40.8
# 60.5

# EXPLANATION:
# isinstance(value, float) checks whether a value is a float.
# If the condition is true, yield returns that value.
# Integer and string values are ignored.


# ============================================================
# Q3. WAGP which yields prime numbers from 1 to 100.
# ============================================================

# ANSWER:

def prime_numbers():
    for num in range(2, 101):
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num

for num in prime_numbers():
    print(num, end=" ")

# OUTPUT:
# 2 3 5 7 11 13 17 19 23 29
# 31 37 41 43 47 53 59 61 67 71
# 73 79 83 89 97

# EXPLANATION:
# A prime number has exactly two factors: 1 and itself.
# range(2, 101) checks numbers from 2 to 100.
# The inner loop checks whether the number is divisible
# by any number from 2 up to its square root.
# If no divisor is found, yield returns the prime number.
# 1 is not a prime number.


# ============================================================
# Q4. WAGF that yields the square of each number from 1 to n.
# ============================================================

# ANSWER:

def square_numbers(n):
    for i in range(1, n + 1):
        yield i ** 2

for num in square_numbers(5):
    print(num, end=" ")

# OUTPUT:
# 1 4 9 16 25

# EXPLANATION:
# The function accepts n as an argument.
# range(1, n + 1) generates numbers from 1 to n.
# ** 2 calculates the square of each number.
# yield returns each square one at a time.


# ============================================================
# Q5. WAGF that counts down from n to 1.
# ============================================================

# ANSWER:

def countdown(n):
    while n >= 1:
        yield n
        n = n - 1

for num in countdown(5):
    print(num, end=" ")

# OUTPUT:
# 5 4 3 2 1

# EXPLANATION:
# The while loop runs until n becomes less than 1.
# yield returns the current value of n.
# n = n - 1 decreases the number by one each time.


# ============================================================
# Q6. WAGF that yields one character at a time from a string.
# ============================================================

# ANSWER:

def characters(text):
    for char in text:
        yield char

for ch in characters("PYTHON"):
    print(ch)

# OUTPUT:
# P
# Y
# T
# H
# O
# N

# EXPLANATION:
# The for loop reads each character from the string.
# yield returns one character at a time.
# The generator does not need to create a separate list.


# ============================================================
# Q7. WAGF my_range(start, stop, step) that works like
# Python's built-in range() function using yield.
# ============================================================

# ANSWER:

def my_range(start, stop, step):
    if step == 0:
        raise ValueError("Step cannot be zero")

    if step > 0:
        while start < stop:
            yield start
            start = start + step

    else:
        while start > stop:
            yield start
            start = start + step

for num in my_range(1, 10, 2):
    print(num, end=" ")

print()

for num in my_range(10, 0, -2):
    print(num, end=" ")

# OUTPUT:
# 1 3 5 7 9
# 10 8 6 4 2

# EXPLANATION:
# start = Starting value.
# stop = Ending limit (not included).
# step = Difference between consecutive values.
# Positive step increases the value.
# Negative step decreases the value.
# yield returns each value one at a time.
# Step cannot be zero because it would cause an infinite loop.


# ============================================================
# Q8. E-COMMERCE ORDER PROCESSING USING GENERATOR
# ============================================================

# QUESTION:
# An e-commerce platform receives thousands of orders every minute.
# To reduce memory usage, orders should be processed one at a time.
#
# Write a generator that yields one order at a time.
# Then write code to process each order as it is received.

# ANSWER:

orders = [
    "ORDER101",
    "ORDER102",
    "ORDER103",
    "ORDER104",
    "ORDER105"
]

def order_generator(orders):
    for order in orders:
        yield order

def process_order(order):
    print("Processing Order:", order)
    print("Order Completed Successfully!")
    print("----------------------------")

for order in order_generator(orders):
    process_order(order)

# OUTPUT:
# Processing Order: ORDER101
# Order Completed Successfully!
# ----------------------------
# Processing Order: ORDER102
# Order Completed Successfully!
# ----------------------------
# Processing Order: ORDER103
# Order Completed Successfully!
# ----------------------------
# Processing Order: ORDER104
# Order Completed Successfully!
# ----------------------------
# Processing Order: ORDER105
# Order Completed Successfully!
# ----------------------------

# EXPLANATION:
# orders contains the order details.
# order_generator() is a generator function.
# yield returns one order at a time.
# process_order() processes the received order.
# The for loop gets the next order and processes it.
#
# BENEFIT:
# Generators avoid creating another complete collection
# of processed orders in memory.
# This approach is useful for processing large datasets.


# ============================================================
# QUICK REVISION – GENERATORS
# ============================================================

# 1. Generator:
# A function that produces values one at a time.

# 2. yield:
# Returns a value and pauses the function execution.

# 3. return:
# Returns a final result and terminates the function.

# 4. next():
# Retrieves the next value from a generator.

# 5. iter():
# Creates an iterator from an iterable object.

# 6. Memory:
# Generators can save memory by producing values on demand.

# END OF GENERATOR PRACTICE
