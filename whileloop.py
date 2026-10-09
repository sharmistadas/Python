
# Q1. WAP to print your name 5 times using while loop

i = 1
while i <= 5:
    print("Sharmistha")
    i += 1

# Output:
# Sharmistha
# Sharmistha
# Sharmistha
# Sharmistha
# Sharmistha



# Q2. WAP to print a sequence of numbers using while loop

i = 1
while i <= 10:
    print(i)
    i += 1

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# Q3. WAP to find the sum of n numbers using while loop

n = int(input("Enter a number: "))
i = 1
total = 0

while i <= n:
    total = total + i
    i += 1

print("Sum =", total)

# Output:
# Enter a number: 5
# Sum = 15
#
# Explanation:
# 1 + 2 + 3 + 4 + 5 = 15
