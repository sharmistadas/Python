
# Q1. Material Quality Classification

score = 75

if score < 40:
    result = "Rejected"
elif score <= 60:
    result = "Acceptable"
elif score <= 80:
    result = "Good"
else:
    result = "Excellent"

print(f"Q1. Material Quality: {result}")

# Output: Material Quality: Good


# Q2. Count Total Characters in a File

# Create sample.txt with: Hello Python

with open("sample.txt", "r") as file:
    content = file.read()
print(f"Q2. Total Characters: {len(content)}")

# Output: Total Characters: 12


# Q3. Count Total Words in a File

with open("sample.txt", "r") as file:
    content = file.read()
words = content.split()
print(f"Q3. Total Words: {len(words)}")

# Output: Total Words: 2


# Q4. Insurance Policy Renewal (Nested if)

renewal = "yes"
grace = "yes"

if renewal == "yes":
    if grace == "yes":
        print("Q4. Policy Renewal: Possible")
    else:
        print("Q4. Policy Renewal: Not Possible")
else:
    print("Q4. Renewal Not Requested")

# Output: Policy Renewal: Possible


# Q6. Fuel Consumption Classification
# Assumed categories: Below 8 = Low, 8 = Moderate,
# Above 8 = High

fuel = 6.5

if fuel < 8:
    category = "Low"
elif fuel == 8:
    category = "Moderate"
else:
    category = "High"

print(f"Q6. Fuel Category: {category}")

# Output: Fuel Category: Low


# Q7. Cloud Backup Restoration (Nested if)

backup = "yes"
integrity = "yes"

if backup == "yes":
    if integrity == "yes":
        print("Q7. Restoration can begin")
    else:
        print("Q7. Integrity verification failed")
else:
    print("Q7. Backup file not found")

# Output: Restoration can begin


# Q8. Apply 10% Discount Using Dictionary Comprehension

products = {
    "Mobile": 20000,
    "Laptop": 50000,
    "Tablet": 15000
}

discounted = {
    product: price * 0.90
    for product, price in products.items()
}

print("Q8. Discounted Products:")

for product, price in discounted.items():
    print(f"{product}: Rs.{price:.2f}")

# Output:
# Mobile: Rs.18000.00
# Laptop: Rs.45000.00
# Tablet: Rs.13500.00


# Q9 (Set A). Customer Exchange Request (Nested if)

exchange = "yes"
receipt = "yes"

if exchange == "yes":
    if receipt == "yes":
        print("Q9 A. Exchange Request: Accepted")
    else:
        print("Q9 A. Receipt Required")
else:
    print("Q9 A. No Exchange Requested")

# Output: Exchange Request: Accepted


# Q10 (Set A). Free Delivery Eligibility

amount = 750

if amount >= 500:
    print("Q10 A. Free Delivery")
else:
    print("Q10 A. Delivery Charges Applicable")

# Output: Free Delivery


# Q9 (Set B). Extract Vowels Using List Comprehension

text = "Python Programming"

vowels = [ch for ch in text if ch.lower() in "aeiou"]

print(f"Q9 B. Vowels: {vowels}")
print(f"Total Vowels: {len(vowels)}")

# Output:
# Vowels: ['o', 'o', 'a', 'i']
# Total Vowels: 4


# Q10 (Set B). School Admission Eligibility

age = 6

if age >= 5:
    print("Q10 B. Eligible for Admission")
else:
    print("Q10 B. Not Eligible for Admission")

# Output: Eligible for Admission


