
# Q1. WAP TO REVERSE A STRING


s = "Python"
i = 0
rev = ""

while i < len(s):
    char = s[i]
    rev = char + rev
    i += 1

print("Reverse string:", rev)

# Output:
# Reverse string: nohtyP



# Q2. WAP TO CHECK WHETHER A STRING IS PALINDROME OR NOT


s = "Malayalam".lower()
i = 0
rev = ""

while i < len(s):
    char = s[i]
    rev = char + rev
    i += 1

if rev == s:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")

# Output:
# malayalam is a palindrome



# Q3. WAP TO REVERSE A NUMBER WITHOUT TYPECASTING


n = 143
res = 0

while n != 0:
    a = n % 10
    res = res * 10 + a
    n = n // 10

print("Reverse number:", res)

# Output:
# Reverse number: 341



# Q4. WAP TO CHECK WHETHER A NUMBER IS PRIME OR NOT


n = 7
i = 1
count = 0

while i <= n:
    if n % i == 0:
        count += 1
    i += 1

if count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

# Output:
# 7 is a prime number



# Q5. WAP TO REPLACE SPACES IN A STRING WITH UNDERSCORES


s = "Python is fun"
i = 0
res = ""

while i < len(s):
    if s[i] == " ":
        res = res + "_"
    else:
        res = res + s[i]
    i += 1

print("Updated string:", res)

# Output:
# Updated string: Python_is_fun


# Q6. WAP TO COUNT THE OCCURRENCES OF SPECIAL CHARACTERS


s = "Pyth!@h"
i = 0
count = 0

while i < len(s):
    if not s[i].isalnum() and not s[i].isspace():
        count += 1
    i += 1

print("Special character count:", count)

# Output:
# Special character count: 2



