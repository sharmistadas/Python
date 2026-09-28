# Not Equal to (!=) operator
#===================================================================#

# INT != INT
print(10 != 20)                    # True

# FLOAT != FLOAT
print(10.5 != 20.5)                # True

# COMPLEX != COMPLEX
print((10+2j) != (20+2j))          # True

# BOOL != BOOL
print(True != False)               # True

# STRING != STRING
print("Python" != "Java")          # True

# LIST != LIST
print([10, 20] != [30, 40])        # True

# TUPLE != TUPLE
print((10, 20) != (30, 40))        # True

# SET != SET
print({10, 20} != {30, 40})        # True

# DICTIONARY != DICTIONARY
print({"a": 10} != {"b": 20})      # True

#===================================================================#

print(10 != 20)        # True
print(10 != 10)        # False

print("Python" != "Java")      # True
print("Python" != "Python")    # False