# INT.................

print(int(500))#500
print(float(300))#300.0
print(complex(-125)) #(-125+0j)

# FLOAT.................

print(int(25.5))              # 25
print(float(25.5))            # 25.5
print(complex(25.5))           # (25.5+0j)
print(bool(25.5))              # True
print(str(25.5))               # 25.5
print(list("25.5"))            # Error
print(tuple("25.5"))           # Error
print(set("25.5"))             # Error
print(dict(value=25.5))        # Error


# COMPLEX.................

print(int(25+5j))              # Error
print(float(25+5j))            # Error
print(complex(25+5j))           # (25+5j)
print(bool(25+5j))              # True
print(str(25+5j))               # (25+5j)
print(list("25+5j"))            # Error
print(tuple("25+5j"))           # Error
print(set("25+5j"))             # Error
print(dict(value=25+5j))        # Error
#Important: complex → int and complex → float are not possible directly, so they give TypeError.

# BOOL.................

print(int(True))                # 1
print(float(True))              # 1.0
print(complex(True))             # (1+0j)
print(bool(True))                # True
print(str(True))                 # True
print(list("True"))              # Error
print(set("True"))               # Error
print(dict(value=True))          # Error

print(int(False))                # 0
print(float(False))              # 0.0
print(complex(False))            # 0j
print(bool(False))               # False
print(str(False))                # False

# STRING value INT.................

print(int(25))                 # 25
print(float(25))               # 25.0
print(complex(25))             # (25+0j)
print(bool(25))                # True
print(str(25))                 # 25
print(list(25))                # TypeError: 'int' object is not iterable
print(tuple(25))               # TypeError: 'int' object is not iterable
print(set(25))                 # TypeError: 'int' object is not iterable
print(dict(25))                # TypeError: 'int' object is not iterable

# STRING value = "A"
print(int("A"))                # ValueError
print(float("A"))              # ValueError
print(complex("A"))            # ValueError
print(bool("A"))               # True
print(str("A"))                # A
print(list("A"))               # ['A']
print(tuple("A"))              # ('A',)
print(set("A"))                # {'A'}
print(dict("A"))               # ValueError


# LIST.................

print(int([10, 20, 30]))              # TypeError
print(float([10, 20, 30]))            # TypeError
print(complex([10, 20, 30]))          # TypeError
print(bool([10, 20, 30]))             # True
print(str([10, 20, 30]))              # [10, 20, 30]
print(list([10, 20, 30]))             # [10, 20, 30]
print(tuple([10, 20, 30]))            # (10, 20, 30)
print(set([10, 20, 30]))              # {10, 20, 30}
print(dict([("a", 10), ("b", 20)]))   # Error

# TUPLE.................

print(int((10, 20, 30)))              # TypeError
print(float((10, 20, 30)))            # TypeError
print(complex((10, 20, 30)))          # TypeError
print(bool((10, 20, 30)))             # True
print(str((10, 20, 30)))              # (10, 20, 30)
print(list((10, 20, 30)))             # [10, 20, 30]
print(tuple((10, 20, 30)))            # (10, 20, 30)
print(set((10, 20, 30)))              # {10, 20, 30}
print(dict(((1, "A"), (2, "B"))))     # TypeError

#Note: int(), float(), and complex() cannot directly convert a tuple containing multiple values.

# SET.................

print(int({10, 20, 30}))              # TypeError
print(float({10, 20, 30}))            # TypeError
print(complex({10, 20, 30}))          # TypeError
print(bool({10, 20, 30}))             # True
print(str({10, 20, 30}))              # {10, 20, 30}
print(list({10, 20, 30}))             # [10, 20, 30]
print(tuple({10, 20, 30}))            # (10, 20, 30)
print(set({10, 20, 30}))              # {10, 20, 30}
print(dict({10, 20, 30}))             # TypeError

#A set can be converted to a dictionary only when its elements are key-value pairs:

# DICTIONARY.................

print(int({"name": "Sharmistha", "age": 24}))       # TypeError
print(float({"name": "Sharmistha", "age": 24}))     # TypeError
print(complex({"name": "Sharmistha", "age": 24}))   # TypeError
print(bool({"name": "Sharmistha", "age": 24}))      # True
print(str({"name": "Sharmistha", "age": 24}))       # {'name': 'Sharmistha', 'age': 24}
print(list({"name": "Sharmistha", "age": 24}))      # ['name', 'age']
print(tuple({"name": "Sharmistha", "age": 24}))     # ('name', 'age')
print(set({"name": "Sharmistha", "age": 24}))       # {'name', 'age'}
print(dict({"name": "Sharmistha", "age": 24}))      # {'name': 'Sharmistha', 'age': 24}