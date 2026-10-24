
# ============================================================
# 1. SPY NUMBER
# Sum of digits == Product of digits
# Input: 1124 | Output: Spy Number
# ============================================================

# WHILE LOOP
n = 1124
temp = n
total = 0
product = 1

while temp > 0:
    digit = temp % 10
    total += digit
    product *= digit
    temp //= 10

if total == product:
    print("Spy Number")
else:
    print("Not a Spy Number")

# FOR LOOP
n = 1124
total = 0
product = 1

for digit in str(n):
    total += int(digit)
    product *= int(digit)

if total == product:
    print("Spy Number")
else:
    print("Not a Spy Number")


# ============================================================
# 2. DUCK NUMBER
# Number contains zero, but does not start with zero
# Input: 1023 | Output: Duck Number
# ============================================================

# WHILE LOOP
n = 1023
temp = n
found = False

while temp > 0:
    if temp % 10 == 0:
        found = True
    temp //= 10

if n > 0 and found:
    print("Duck Number")
else:
    print("Not a Duck Number")

# FOR LOOP
n = 1023
found = False

for digit in str(n):
    if digit == "0":
        found = True

if n > 0 and found:
    print("Duck Number")
else:
    print("Not a Duck Number")


# ============================================================
# 3. AUTOMORPHIC NUMBER
# Square ends with the original number
# Input: 25 | Output: Automorphic Number
# ============================================================

# WHILE LOOP
n = 25
square = n * n
temp = n
divisor = 1

while temp > 0:
    divisor *= 10
    temp //= 10

if square % divisor == n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

# FOR LOOP
n = 25
square = n * n
divisor = 1

for digit in str(n):
    divisor *= 10

if square % divisor == n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")


# ============================================================
# 4. TRIMORPHIC NUMBER
# Cube ends with the original number
# Input: 24 | Output: Trimorphic Number
# ============================================================

# WHILE LOOP
n = 24
cube = n ** 3
temp = n
divisor = 1

while temp > 0:
    divisor *= 10
    temp //= 10

if cube % divisor == n:
    print("Trimorphic Number")
else:
    print("Not a Trimorphic Number")

# FOR LOOP
n = 24
cube = n ** 3
divisor = 1

for digit in str(n):
    divisor *= 10

if cube % divisor == n:
    print("Trimorphic Number")
else:
    print("Not a Trimorphic Number")


# ============================================================
# 5. NEON NUMBER
# Sum of square's digits == Original number
# Input: 9 | Output: Neon Number
# ============================================================

# WHILE LOOP
n = 9
temp = n * n
total = 0

while temp > 0:
    total += temp % 10
    temp //= 10

if total == n:
    print("Neon Number")
else:
    print("Not a Neon Number")

# FOR LOOP
n = 9
total = 0

for digit in str(n * n):
    total += int(digit)

if total == n:
    print("Neon Number")
else:
    print("Not a Neon Number")


# ============================================================
# 6. HARSHAD NUMBER
# Number is divisible by the sum of its digits
# Input: 18 | Output: Harshad Number
# ============================================================

# WHILE LOOP
n = 18
temp = n
total = 0

while temp > 0:
    total += temp % 10
    temp //= 10

if n > 0 and n % total == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")

# FOR LOOP
n = 18
total = 0

for digit in str(n):
    total += int(digit)

if n > 0 and n % total == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")


# ============================================================
# 7. PRONIC NUMBER
# Product of two consecutive non-negative integers
# Input: 42 | Output: Pronic Number (6 * 7)
# ============================================================

# WHILE LOOP
n = 42
i = 0
found = False

while i * (i + 1) <= n:
    if i * (i + 1) == n:
        found = True
        break
    i += 1

if found:
    print("Pronic Number:", i, "*", i + 1, "=", n)
else:
    print("Not a Pronic Number")

# FOR LOOP
n = 42
found = False

for i in range(n + 1):
    if i * (i + 1) == n:
        found = True
        break

if found:
    print("Pronic Number:", i, "*", i + 1, "=", n)
else:
    print("Not a Pronic Number")


# ============================================================
# 8. DISARIUM NUMBER
# Sum of digits raised to their left-to-right positions
# Input: 135 | Output: Disarium Number
# ============================================================

# WHILE LOOP
n = 135
temp = n
digits = 0

while temp > 0:
    digits += 1
    temp //= 10

temp = n
total = 0
position = digits

while temp > 0:
    digit = temp % 10
    total += digit ** position
    position -= 1
    temp //= 10

if total == n:
    print("Disarium Number")
else:
    print("Not a Disarium Number")

# FOR LOOP
n = 135
total = 0

for position, digit in enumerate(str(n), start=1):
    total += int(digit) ** position

if total == n:
    print("Disarium Number")
else:
    print("Not a Disarium Number")
