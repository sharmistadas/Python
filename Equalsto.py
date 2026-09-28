# Equal to (==) operator
#===================================================================#

# INT == INT
print(10 == 10)                    # True
# FLOAT == FLOAT
print(10.5 == 10.5)                # True
# COMPLEX == COMPLEX
print((10+2j) == (10+2j))          # True
# BOOL == BOOL
print(True == True)                # True
# STRING == STRING
print("Python" == "Python")        # True
# LIST == LIST
print([10, 20] == [10, 20])        # True
# TUPLE == TUPLE
print((10, 20) == (10, 20))        # True
# SET == SET
print({10, 20} == {10, 20})        # True
# DICTIONARY == DICTIONARY
print({"a": 10} == {"a": 10})      # True

#===================================================================#

print(10 == 20)                    # False
print(10.5 == 20.5)                # False
print((10+2j) == (20+2j))          # False
print(True == False)               # False
print("Python" == "Java")          # False
print([10, 20] == [30, 40])        # False
print((10, 20) == (30, 40))        # False
print({10, 20} == {30, 40})        # False
print({"a": 10} == {"b": 20})      # False