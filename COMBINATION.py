# =====================================================================
#                         OPERATORS
# =====================================================================


# 1) ADDITION OPERATOR (+)
print(25 + 15)                         # Output: 40
# + is used to add two values.


# 2) SUBTRACTION OPERATOR (-)
print(50 - 18)                         # Output: 32
# - is used to subtract the second value from the first value.


# 3) MULTIPLICATION OPERATOR (*)
print(7 * 8)                            # Output: 56
# * is used to multiply two values.


# 4) DIVISION OPERATOR (/)
print(45 / 5)                           # Output: 9.0
# / always gives the result in float.


# 5) FLOOR DIVISION OPERATOR (//)
print(29 // 4)                         # Output: 7
# // gives the quotient without the decimal part.


# 6) MODULUS OPERATOR (%)
print(29 % 4)                          # Output: 1
# % gives the remainder.


# 7) POWER / EXPONENT OPERATOR (**)
print(3 ** 4)                          # Output: 81
# ** means power. 3^4 = 3 × 3 × 3 × 3 = 81.


# 8) OPERATOR PRECEDENCE
print(10 + 5 * 3)                      # Output: 25
# Multiplication (*) is performed before addition (+).


# 9) PARENTHESES
print((10 + 5) * 3)                    # Output: 45
# Parentheses are performed first.


# 10) FLOOR DIVISION + ADDITION
print(100 // 6 + 4)                    # Output: 20
# First 100 // 6 = 16, then 16 + 4 = 20.


# =====================================================================
#                     RELATIONAL / COMPARISON OPERATORS
# =====================================================================


# 11) GREATER THAN (>)
print(15 > 10)                         # Output: True
# 15 is greater than 10.


# 12) LESS THAN (<)
print(25 < 20)                         # Output: False
# 25 is not less than 20.


# 13) EQUAL TO (==)
print(50 == 50)                        # Output: True
# Both values are equal.


# 14) NOT EQUAL TO (!=)
print(30 != 25)                        # Output: True
# 30 and 25 are not equal.


# 15) GREATER THAN OR EQUAL TO (>=)
print(40 >= 40)                        # Output: True
# 40 is equal to 40, so the condition is True.


# 16) LESS THAN OR EQUAL TO (<=)
print(15 <= 10)                        # Output: False
# 15 is neither less than nor equal to 10.


# 17) ADDITION + EQUAL TO
print(10 + 5 == 15)                   # Output: True
# 10 + 5 = 15, so the comparison is True.


# 18) MULTIPLICATION + NOT EQUAL TO
print(20 * 2 != 50)                   # Output: True
# 20 * 2 = 40, and 40 is not equal to 50.


# =====================================================================
#                       LOGICAL OPERATORS
# =====================================================================


# 19) AND
print(True and False)                  # Output: False
# AND gives True only when both conditions are True.


# 20) OR
print(True or False)                   # Output: True
# OR gives True when at least one condition is True.


# 21) NOT
print(not True)                        # Output: False
# not changes True to False.


# 22) NOT
print(not False)                       # Output: True
# not changes False to True.


# 23) AND WITH CONDITIONS
print(10 > 5 and 20 > 15)              # Output: True
# Both conditions are True.


# 24) OR WITH CONDITIONS
print(10 < 5 or 20 > 15)               # Output: True
# First condition is False, second condition is True.
# OR gives True because one condition is True.


# 25) NOT WITH CONDITION
print(not (10 > 5))                    # Output: False
# 10 > 5 is True, and not True becomes False.


# 26) AND + OR
print(False or True and False)          # Output: False
# AND is performed before OR.
# True and False = False
# False or False = False


# =====================================================================
#                       BITWISE OPERATORS
# =====================================================================


# 27) BITWISE AND (&)
print(5 & 3)                           # Output: 1
# 5 = 101
# 3 = 011
# AND = 001 = 1


# 28) BITWISE OR (|)
print(5 | 3)                           # Output: 7
# 5 = 101
# 3 = 011
# OR = 111 = 7


# 29) BITWISE XOR (^)
print(5 ^ 3)                           # Output: 6
# 5 = 101
# 3 = 011
# XOR = 110 = 6


# 30) LEFT SHIFT (<<)
print(8 << 2)                          # Output: 32
# Left shift by 2 positions.
# 8 × 2^2 = 32


# 31) RIGHT SHIFT (>>)
print(16 >> 2)                         # Output: 4
# Right shift by 2 positions.
# 16 // 2^2 = 4


# 32) BITWISE NOT (~)
print(~5)                              # Output: -6
# Formula: ~n = -(n + 1)
# ~5 = -(5 + 1) = -6


# =====================================================================
#                       ASSIGNMENT OPERATORS
# =====================================================================


# 33) ADD AND ASSIGN (+=)
x = 20
x += 10
print(x)                               # Output: 30
# x += 10 means x = x + 10.


# 34) SUBTRACT AND ASSIGN (-=)
x = 20
x -= 7
print(x)                               # Output: 13
# x -= 7 means x = x - 7.


# 35) MULTIPLY AND ASSIGN (*=)
x = 5
x *= 3
print(x)                               # Output: 15
# x *= 3 means x = x * 3.


# 36) DIVIDE AND ASSIGN (/=)
x = 20
x /= 4
print(x)                               # Output: 5.0
# x /= 4 means x = x / 4.


# 37) FLOOR DIVIDE AND ASSIGN (//=)
x = 20
x //= 3
print(x)                               # Output: 6
# x //= 3 means x = x // 3.


# 38) MODULUS AND ASSIGN (%=)
x = 20
x %= 6
print(x)                               # Output: 2
# x %= 6 means x = x % 6.


# 39) POWER AND ASSIGN (**=)
x = 5
x **= 2
print(x)                               # Output: 25
# x **= 2 means x = x ** 2.


# 40) BITWISE AND AND ASSIGN (&=)
x = 5
x &= 7
print(x)                               # Output: 5
# x &= 7 means x = x & 7.
# 5 & 7 = 5.


# =====================================================================
#                       MEMBERSHIP OPERATORS
# =====================================================================


# 41) IN
print("Python" in ["Java", "Python", "C++"])       # Output: True
# "Python" is present in the list.


# 42) NOT IN
print("Java" not in ["Python", "C++", "JavaScript"])  # Output: True
# "Java" is not present in the list.


# 43) IN
print(10 in [5, 10, 15, 20])                       # Output: True
# 10 is present in the list.


# 44) NOT IN
print(25 not in [10, 20, 30, 40])                   # Output: True
# 25 is not present in the list.


# =====================================================================
#                       IDENTITY OPERATORS
# =====================================================================


# 45) IS
x = [1, 2, 3]
y = x

print(x is y)                                      # Output: True
# x and y refer to the same list object.


# 46) IS
x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)                                      # Output: False
# Values are same, but both are different list objects.


# 47) IS NONE
x = None

print(x is None)                                   # Output: True
# x contains the special value None.


# 48) IS NOT
x = 10
y = 10

print(x is not y)                                  # Output: False
# For these small integers, Python may use the same cached object.
# Therefore x is y is True, so x is not y is False.


# =====================================================================
#                         COMBINATION
# =====================================================================


# 49) ARITHMETIC + COMPARISON + LOGICAL
print(10 + 5 * 2 > 15 and 20 != 10)               # Output: True
# 5 * 2 = 10
# 10 + 10 = 20
# 20 > 15 = True
# 20 != 10 = True
# True and True = True


# 50) FLOOR DIVISION + MODULUS + OR
print(25 // 4 + 3 == 9 or 10 % 3 == 1)             # Output: True
# 25 // 4 = 6
# 6 + 3 = 9
# 9 == 9 = True
# OR makes the complete result True.


# 51) AND + OR + NOT
print(5 > 2 and 10 < 20 or not False)              # Output: True
# 5 > 2 = True
# 10 < 20 = True
# True and True = True
# not False = True
# True or True = True


# 52) BITWISE + COMPARISON + OR
print(8 & 3 == 0 or 5 | 2 > 6)                     # Output: True
# 8 & 3 = 0
# 0 == 0 = True
# Therefore the complete result is True.


# 53) ARITHMETIC + COMPARISON + AND
print(10 + 5 * 2 >= 20 and 15 % 4 == 3)            # Output: True
# 5 * 2 = 10
# 10 + 10 = 20
# 20 >= 20 = True
# 15 % 4 = 3
# 3 == 3 = True
# True and True = True


# 54) NOT + FLOOR DIVISION + AND + OR
print(not (10 > 5) or 20 // 3 == 6 and 5 != 2)     # Output: True
# 10 > 5 = True
# not True = False
# 20 // 3 = 6
# 6 == 6 = True
# 5 != 2 = True
# True and True = True
# False or True = True


# 55) BITWISE AND + BITWISE OR + AND
print(5 & 3 == 1 and 10 | 2 == 10)                 # Output: True
# 5 & 3 = 1
# 1 == 1 = True
# 10 | 2 = 10
# 10 == 10 = True
# True and True = True


# 56) POWER + MULTIPLICATION + OR
print(2 ** 3 + 4 * 2 == 16 or 15 // 4 == 3)        # Output: True
# 2 ** 3 = 8
# 4 * 2 = 8
# 8 + 8 = 16
# 16 == 16 = True
# Therefore complete result is True.


# 57) MEMBERSHIP + COMPARISON + AND
print("Python" in ["Java", "Python", "C++"] and 10 > 5)
# Output: True
# "Python" is present in the list = True
# 10 > 5 = True
# True and True = True


# 58) MEMBERSHIP + MODULUS + AND + OR
print("Java" not in ["Python", "C++"] or 20 % 6 == 2 and 5 < 10)
# Output: True
# "Java" is not in the list = True
# Because OR has one True condition, final result is True.


# 59) IDENTITY + LEN + AND
x = [1, 2, 3]
y = x

print(x is y and len(x) == 3)                       # Output: True
# x and y refer to the same object = True
# Length of x is 3 = True
# True and True = True


# 60) IDENTITY + MEMBERSHIP + COMPARISON
x = [10, 20]
y = [10, 20]

print(x is not y and 10 in x and 20 > 15)           # Output: True
# x and y are different objects = True
# 10 is present in x = True
# 20 > 15 = True
# True and True and True = True