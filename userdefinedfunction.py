
# ============================================================
# TYPE 1: WITHOUT ARGUMENT - WITHOUT RETURN
# No arguments are passed and no value is returned.
# Results are displayed using print().
# ============================================================

# 1. Print Hello Python
def greeting():
    print("Hello, Python!")

greeting()


# 2. Print numbers from 1 to 20
def numbers():
    for i in range(1, 21):
        print(i, end=" ")
    print()

numbers()


# 3. Print even numbers from 1 to 50
def even_numbers():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i, end=" ")
    print()

even_numbers()


# 4. Print odd numbers from 1 to 50
def odd_numbers():
    for i in range(1, 51):
        if i % 2 != 0:
            print(i, end=" ")
    print()

odd_numbers()


# 5. Print multiplication table of 5
def multiplication_table():
    for i in range(1, 11):
        print(5, "*", i, "=", 5 * i)

multiplication_table()


# 6. Print prime numbers from 1 to 100
def prime_numbers():
    for num in range(2, 101):
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            print(num, end=" ")
    print()

prime_numbers()


# 7. Print squares from 1 to 10
def squares():
    for i in range(1, 11):
        print(i, "square =", i * i)

squares()


# 8. Print sum from 1 to 10
def sum_numbers():
    total = 0

    for i in range(1, 11):
        total = total + i

    print("Sum =", total)

sum_numbers()


# 9. Print numbers divisible by both 3 and 5
def divisible_numbers():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
    print()

divisible_numbers()


# 10. Print factorial of 5
def factorial_five():
    fact = 1

    for i in range(1, 6):
        fact = fact * i

    print("Factorial =", fact)

factorial_five()


# ============================================================
# TYPE 2: WITH ARGUMENT - WITHOUT RETURN
# Arguments are passed to the function.
# Results are displayed using print().
# No value is returned.
# ============================================================

# 1. Check positive, negative or zero
def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

check_number(-5)


# 2. Check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(10)


# 3. Sum of two numbers
def add(a, b):
    print("Sum =", a + b)

add(10, 20)


# 4. Multiplication table
def table(num):
    for i in range(1, 11):
        print(num, "*", i, "=", num * i)

table(7)


# 5. Factorial of a number
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial =", fact)

factorial(5)


# 6. Check prime or not
def check_prime(num):
    if num < 2:
        print("Not Prime")
        return

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Prime")
    else:
        print("Not Prime")

check_prime(7)


# 7. Reverse a string
def reverse_string(text):
    reverse = ""

    for char in text:
        reverse = char + reverse

    print("Reverse =", reverse)

reverse_string("Python")


# 8. Count vowels in a string
def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    print("Vowels =", count)

count_vowels("Education")


# 9. Largest among three numbers
def largest(a, b, c):
    if a >= b and a >= c:
        print("Largest =", a)
    elif b >= a and b >= c:
        print("Largest =", b)
    else:
        print("Largest =", c)

largest(10, 30, 20)


# 10. Check leap year
def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

leap_year(2024)


# ============================================================
# TYPE 3: WITHOUT ARGUMENT - WITH RETURN
# No arguments are passed.
# The function calculates and returns a value.
# The caller uses print() to display the returned value.
# ============================================================

# 1. Return sum from 1 to 10
def get_sum():
    total = 0

    for i in range(1, 11):
        total += i

    return total

print("Sum =", get_sum())


# 2. Return multiplication of 10 and 20
def get_multiplication():
    return 10 * 20

print("Multiplication =", get_multiplication())


# 3. Return factorial of 5
def get_factorial():
    fact = 1

    for i in range(1, 6):
        fact *= i

    return fact

print("Factorial =", get_factorial())


# 4. Return largest among 10, 20 and 30
def get_largest():
    a, b, c = 10, 20, 30

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Largest =", get_largest())


# 5. Return sum of even numbers from 1 to 50
def get_even_sum():
    total = 0

    for i in range(1, 51):
        if i % 2 == 0:
            total += i

    return total

print("Even Sum =", get_even_sum())


# 6. Return sum of odd numbers from 1 to 50
def get_odd_sum():
    total = 0

    for i in range(1, 51):
        if i % 2 != 0:
            total += i

    return total

print("Odd Sum =", get_odd_sum())


# 7. Return count of numbers divisible by 5
def get_count():
    count = 0

    for i in range(1, 101):
        if i % 5 == 0:
            count += 1

    return count

print("Count =", get_count())


# 8. Return reverse of Python
def get_reverse():
    text = "Python"
    reverse = ""

    for char in text:
        reverse = char + reverse

    return reverse

print("Reverse =", get_reverse())


# 9. Return sum of digits of 12345
def get_digit_sum():
    num = 12345
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total

print("Digit Sum =", get_digit_sum())


# 10. Return number of vowels in Education
def get_vowel_count():
    text = "Education"
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count

print("Vowel Count =", get_vowel_count())


# ============================================================
# TYPE 4: WITH ARGUMENT - WITH RETURN
# Arguments are passed to the function.
# The function calculates and returns the result.
# The caller displays the result using print().
# ============================================================

# 1. Return square of a number
def square(num):
    return num * num

print("Square =", square(5))


# 2. Return cube of a number
def cube(num):
    return num * num * num

print("Cube =", cube(3))


# 3. Return sum of two numbers
def addition(a, b):
    return a + b

print("Sum =", addition(10, 20))


# 4. Return largest of two numbers
def get_maximum(a, b):
    if a > b:
        return a
    else:
        return b

print("Largest =", get_maximum(50, 30))


# 5. Return factorial of a number
def find_factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact

print("Factorial =", find_factorial(5))


# 6. Return whether a number is prime or not
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print("Prime =", is_prime(7))


# 7. Return reverse of a string
def reverse(text):
    result = ""

    for char in text:
        result = char + result

    return result

print("Reverse =", reverse("Python"))


# 8. Return sum of digits
def digit_sum(num):
    num = abs(num)
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total

print("Digit Sum =", digit_sum(12345))


# 9. Return number of vowels
def vowels_count(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count

print("Vowel Count =", vowels_count("Education"))


# 10. Return second-largest distinct number in a list
def second_largest(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    if len(unique) < 2:
        return None

    largest = unique[0]
    second = None

    for num in unique:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second

print("Second Largest =", second_largest([10, 50, 30, 40, 50]))


