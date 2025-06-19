# Author: Tanishq Tripathi
# Date: 19/06/2025

a = 10  # Integer
b = 3.14  # Float
c = complex(2, 3)  # Complex number
d = "Hello"  # String   
e = True  # Boolean
f = None  # NoneType   
g = [1, 2, 3]  # List
h = (4, 5, 6)  # Tuple 
i = {7, 8, 9}  # Set
j = {"key": "value"}  # Dictionary
k = bytearray(5)  # Bytearray
l = bytes(5)  # Bytes
m = memoryview(bytes(5))  # Memoryview
n = range(10)  # Range
o = frozenset([10, 20, 30])  # Frozenset
# Printing the types of the variables
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
print(type(d))  # <class 'str'>
print(type(e))  # <class 'bool'>
print(type(f))  # <class 'NoneType'>
print(type(g))  # <class 'list'>
print(type(h))  # <class 'tuple'>
print(type(i))  # <class 'set'>
print(type(j))  # <class 'dict'>
print(type(k))  # <class 'bytearray'>
print(type(l))  # <class 'bytes'>
print(type(m))  # <class 'memoryview'>
print(type(n))  # <class 'range'>
print(type(o))  # <class 'frozenset'>
# Demonstrating the use of type() function
print("The type of variable 'a' is:", type(a))  # The type of variable 'a' is: <class 'int'>
print("The type of variable 'b' is:", type(b))  # The type of variable 'b' is: <class 'float'>
print("The type of variable 'c' is:", type(c))  # The type of variable 'c' is: <class 'complex'>
print("The type of variable 'd' is:", type(d))  # The type of variable 'd' is: <class 'str'>
print("The type of variable 'e' is:", type(e))  # The type of variable 'e' is: <class 'bool'>
print("The type of variable 'f' is:", type(f))  # The type of variable 'f' is: <class 'NoneType'>
print("The type of variable 'g' is:", type(g))  # The type of variable 'g' is: <class 'list'>
print("The type of variable 'h' is:", type(h))  # The type of variable 'h' is: <class 'tuple'>
print("The type of variable 'i' is:", type(i))  # The type of variable 'i' is: <class 'set'>
print("The type of variable 'j' is:", type(j))  # The type of variable 'j' is: <class 'dict'>
print("The type of variable 'k' is:", type(k))  # The type of variable 'k' is: <class 'bytearray'>
print("The type of variable 'l' is:", type(l))  # The type of variable 'l' is: <class 'bytes'>
print("The type of variable 'm' is:", type(m))  # The type of variable 'm' is: <class 'memoryview'>
print("The type of variable 'n' is:", type(n))  # The type of variable 'n' is: <class 'range'>
print("The type of variable 'o' is:", type(o))  # The type of variable 'o' is: <class 'frozenset'>
# Demonstrating the use of isinstance() function
print("Is 'a' an instance of int?", isinstance(a, int))  # Is 'a' an instance of int? True
