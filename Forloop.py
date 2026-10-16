
# 1. WAP to print even numbers from 1 to 10

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# Output:
# 2
# 4
# 6
# 8
# 10


# 2. WAP for password validation
# Length > 8 and < 12, uppercase, lowercase, digit,
# special character required, and no spaces allowed.

pswd = input("Enter password: ")

if (9 <= len(pswd) <= 11
    and any(ch.isupper() for ch in pswd)
    and any(ch.islower() for ch in pswd)
    and any(ch.isdigit() for ch in pswd)
    and any(not ch.isalnum() and not ch.isspace()
            for ch in pswd)
    and not any(ch.isspace() for ch in pswd)):
    print("Valid password")
else:
    print("Invalid password")

# Output 1:
# Enter password: Python@123
# Valid password
# Output 2:
# Enter password: python123
# Invalid password


# 3. WAP to remove duplicate elements from a list

lst = [10, 20, 10, 30, 20, 40, 30]
new_lst = []

for i in lst:
    if i not in new_lst:
        new_lst.append(i)

print(new_lst)

# Output:
# [10, 20, 30, 40]


# 4. WAP to reverse a string without slicing

s = input("Enter a string: ")
rev = ""
i = 0

while i < len(s):
    rev = s[i] + rev
    i += 1

print("Reversed string:", rev)

# Output:
# Enter a string: Python
# Reversed string: nohtyP


# 5. WAP to get the required output

s = "you do not have dasara holidays"
words = s.split()
result = []

for word in words:
    if word == "do":
        continue
    elif word == "not":
        result.append("dont.5")
    elif word == "holidays":
        result.append("holiday.8")
    else:
        result.append(word + "." + str(len(word)))

print(" , ".join(result))

# Output:
# you.3 , dont.5 , have.4 , dasara.6 , holiday.8


# 6. WAP to split a string without using split()

s = input("Enter a string: ")
word = ""
words = []

for ch in s:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""

if word != "":
    words.append(word)

print("Words:", words)

# Output:
# Enter a string: Python is easy to learn
# Words: ['Python', 'is', 'easy', 'to', 'learn']