
# Q1. WAPD to print a message before and after executing a program.

# Answer:

def decorator(func):
    def wrapper():
        print("Before executing the function")
        func()
        print("After executing the function")
    return wrapper

@decorator
def main():
    print("Hello Python")

main()

# Output:
# Before executing the function
# Hello Python
# After executing the function

# Explanation:
# A decorator adds extra functionality to an existing function.
# @decorator applies the decorator to main().
# wrapper() prints a message before and after calling main().


# ============================================================
# Q2. WAPD to return the function name.
# ============================================================

# Answer:

from functools import wraps

def get_function_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func.__name__
    return wrapper

@get_function_name
def main():
    print("Hello Python")

print("Function Name:", main())

# Output:
# Function Name: main

# Explanation:
# __name__ is a special attribute that returns the function name.
# wraps preserves the original function's metadata.
# Here, the decorator returns the original function name.


# ============================================================
# Q3. WAPD to calculate the time taken to execute a program.
# ============================================================

# Answer:

import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print("Execution Time:", end - start, "seconds")
        return result
    return wrapper

@calculate_time
def main():
    total = 0
    for i in range(1000000):
        total = total + i
    print("Total:", total)

main()

# Output:
# Total: 499999500000
# Execution Time: (varies) seconds

# Explanation:
# perf_counter() records a high-resolution time.
# start stores the time before function execution.
# end stores the time after function execution.
# Subtracting start from end gives execution time.


# ============================================================
# Q4. WAPD to delay the main function for 3 seconds.
# ============================================================

# Answer:

import time

def delay(func):
    def wrapper(*args, **kwargs):
        print("Waiting for 3 seconds...")
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper

@delay
def main():
    print("Main function executed successfully!")

main()

# Output:
# Waiting for 3 seconds...
# (3 seconds delay)
# Main function executed successfully!

# Explanation:
# time.sleep(3) pauses program execution for 3 seconds.
# After 3 seconds, the main() function executes.


# ============================================================
# QUICK REVISION
# ============================================================

# 1. Decorator:
# A function that adds extra functionality to another function.

# 2. @decorator:
# Used to apply a decorator to a function.

# 3. __name__:
# Returns the name of a function.

# 4. functools.wraps:
# Preserves the original function's metadata.

# 5. time.perf_counter():
# Measures execution time accurately.

# 6. time.sleep(3):
# Delays execution for 3 seconds.

# END OF DECORATOR PRACTICE
