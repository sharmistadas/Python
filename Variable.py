# ==============================================================================
# 1. VARIABLE-LENGTH POSITIONAL ARGUMENTS (*args)
# ==============================================================================

# Ex 1: Print user-entered values
def add(*args):
    print(args)

add(10, 30)
# Output: (10, 30)[span_0](start_span)[span_0](end_span)

add(4, 5, 2)
# Output: (4, 5, 2)[span_1](start_span)[span_1](end_span)

add(10, 40, 20, 10, 50)
# Output: (10, 40, 20, 10, 50)[span_2](start_span)[span_2](end_span)

add("hello", "world")
# Output: ('hello', 'world')[span_3](start_span)[span_3](end_span)


# Ex 2: WAP to add user-entered values
def sum_values(*args):
    total = 0
    for i in args:
        total += i
    print(total)

sum_values(10, 30)
# Output: 40[span_4](start_span)[span_4](end_span)

sum_values(4, 5, 2)
# Output: 11[span_5](start_span)[span_5](end_span)

sum_values(10, 40, 20, 10, 50)
# Output: 130[span_6](start_span)[span_6](end_span)


# ==============================================================================
# 2. VARIABLE-LENGTH KEYWORD ARGUMENTS (**kwargs)
# ==============================================================================

# Ex 1: Print user-entered values
def func_kwargs(**kwargs):
    print(kwargs)

func_kwargs(a="adhipurush", b="brahmotsavam", c="chennai love story")
# Output: {'a': 'adhipurush', 'b': 'brahmotsavam', 'c': 'chennai love story'}[span_7](start_span)[span_7](end_span)

func_kwargs(d=["devara", "dhammu"], e="eswar", f="funky")
# Output: {'d': ['devara', 'dhammu'], 'e': 'eswar', 'f': 'funky'}[span_8](start_span)[span_8](end_span)

# Error Example: Takes 0 positional arguments
# func_kwargs("gamechanger", "spyder")
# Output: TypeError: func() takes 0 positional arguments but 2 were given[span_9](start_span)[span_9](end_span)


# Ex 2: WAP to print total bill for DMart shopping
def dmart(**items):
    print("Welcome to Dmart")
    print("Items   price")
    price = 0
    for i in items:
        print(i, items[i], sep="   ")
        price += items[i]

    gst = 18
    extra_amt = price * gst / 100
    total_amt = extra_amt + price

    print(f"Total bill with GST --- ₹ {total_amt}/-")
    print("Thank you \n Visit again")

dmart(chocolate=50, coke=40, vim=30)
# Output:
# Welcome to Dmart[span_10](start_span)[span_10](end_span)
# Items   price[span_11](start_span)[span_11](end_span)
# chocolate   50[span_12](start_span)[span_12](end_span)
# coke   40[span_13](start_span)[span_13](end_span)
# vim   30[span_14](start_span)[span_14](end_span)
# Total bill with GST --- ₹ 141.6/-[span_15](start_span)[span_15](end_span)
# Thank you[span_16](start_span)[span_16](end_span)
#  Visit again[span_17](start_span)[span_17](end_span)


# ==============================================================================
# 3. COMBINATION OF POSITIONAL AND KEYWORD ARGUMENTS (*args, **kwargs)
# ==============================================================================

# Ex 1: WAP to order in Blinkit & print total bill
def blinkit(name, *address, **items):
    delivery_charges = 40
    handling_fee = 3

    print(f"Hello {name}")
    print("Confirm your order")
    print("product   price")

    price = 0
    for i in items:
        print(i, items[i], sep="   ")
        price += items[i]

    if price >= 250:
        total_amt = price + handling_fee
    else:
        total_amt = price + handling_fee + delivery_charges

    print(f"Total Amount to pay : ₹ {total_amt}/-")
    print("confirm address")

    l = list(address)
    print(f"Delivery Address : {' '.join(l)}")

blinkit(
    "smithika",
    "3-45", "#26", "6th main 2phase Jntu", "hyd", "500078",
    paste=30, diet_coke=60, chocolate=100, soap=30, shampoo=250,
    notes=50, eggs=200, boost=350, milk=36
)
# Output:
# Hello smithika[span_18](start_span)[span_18](end_span)
# Confirm your order[span_19](start_span)[span_19](end_span)
# product   price[span_20](start_span)[span_20](end_span)
# paste   30[span_21](start_span)[span_21](end_span)
# diet_coke   60[span_22](start_span)[span_22](end_span)
# chocolate   100[span_23](start_span)[span_23](end_span)
# soap   30[span_24](start_span)[span_24](end_span)
# shampoo   250[span_25](start_span)[span_25](end_span)
# notes   50[span_26](start_span)[span_26](end_span)
# eggs   200[span_27](start_span)[span_27](end_span)
# boost   350[span_28](start_span)[span_28](end_span)
# milk   36[span_29](start_span)[span_29](end_span)
# Total Amount to pay : ₹ 1109/-[span_30](start_span)[span_30](end_span)
# confirm address[span_31](start_span)[span_31](end_span)
# Delivery Address : 3-45 #26 6th main 2phase Jntu hyd 500078[span_32](start_span)[span_32](end_span)


# ==============================================================================
# 4. DEFAULT ARGUMENTS
# ==============================================================================

# Ex 1: Missing required arguments
def add_three(a, b, c):
    print(f"a: {a}  b: {b}  c: {c}  addition: {a + b + c}")

# add_three(2, 4)
# Output: TypeError: add() missing 1 required positional argument: 'c[span_33](start_span)'[span_33](end_span)


# Ex 2: Functions with default parameters
def add_defaults(a=10, b=20, c=30):
    print(f"a: {a}  b: {b}  c: {c}  addition: {a + b + c}")

add_defaults()
# Output: a: 10  b: 20  c: 30  addition: 60[span_34](start_span)[span_34](end_span)

add_defaults(35, 60)
# Output: a: 35  b: 60  c: 30  addition: 125[span_35](start_span)[span_35](end_span)

add_defaults(c=15)
# Output: a: 10  b: 20  c: 15  addition: 45[span_36](start_span)[span_36](end_span)


# ==============================================================================
# 5. VARIABLE SCOPE (Local, Global, Non-local)
# ==============================================================================

# --- Local Scope ---
def test_local():
    a = 15
    print(f"local variable inside function: {a}")

test_local()
# Output: local variable inside function: 15[span_37](start_span)[span_37](end_span)

# print(f"local variable outside function: {a}")
# Output: NameError: name 'a' is not defined[span_38](start_span)[span_38](end_span)


# --- Global Scope Access ---
global_a = 100

def test_global():
    print(f"accessing the global variable inside func : {global_a}")

test_global()
# Output: accessing the global variable inside func : 100[span_39](start_span)[span_39](end_span)

print(f"global variable outside the func : {global_a}")
# Output: global variable outside the func : 100[span_40](start_span)[span_40](end_span)


# --- Global Modification without 'global' keyword ---
val = 20

def modify_fail():
    # val += 5
    pass

# modify_fail()
# Output: UnboundLocalError: cannot access local variable 'val' where it is not associated with a value[span_41](start_span)[span_41](end_span)


# --- Global Modification with 'global' keyword ---
a_val = 20

def modify():
    global a_val
    a_val += 5
    print(a_val)

modify()
# Output: 25[span_42](start_span)[span_42](end_span)

print(a_val)
# Output: 25[span_43](start_span)[span_43](end_span)


# --- Banking Simulation Example ---
bal = 1000
acc_num = 123456789
pin = 1432

def deposit(acc, pin_, amt):
    global bal
    if acc_num == acc:
        if pin == pin_:
            if amt >= 100:
                bal += amt
                print("deposited successfully")
            else:
                print("bichagadu")
        else:
            print("incorrect pin")
    else:
        print("acc not found")

deposit(123456789, 1432, 2500)
# Output: deposited successfully[span_44](start_span)[span_44](end_span)

print(f"Available Balance : {bal}")
# Output: Available Balance : 3500[span_45](start_span)[span_45](end_span)




