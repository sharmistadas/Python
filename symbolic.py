# WAP TO CHECK WHETHER USER ENTERED A PIN OF EXACTLY 4 DIGITS

pin = input("Enter the PIN: ")

if len(pin) == 4:
    print("PIN has 4 digits")
else:
    print("PIN does not have 4 digits")


#CHECK WHETHER A CHARACTER IS A VOWEL OR NOT 
ch = input("Enter character:")
if ch in "aeiouAEIOU":
    print ("vowel")
else: 
    print ("Not a vowel")

# check wheter a number is even and a multiple of 5 or not 

num = int (input("Enter number:"))
if num % 2 ==0 and num % 5 ==0 :
    print ("Even and multiple of 5")
else:
    print("Not even and multiple of 5")

# check wheter a character is an alphabet or not 

ch = input("Enter character:")
if ch.isalpha():
    print("Alaphabet")
else:
    print("Not an alphabet")