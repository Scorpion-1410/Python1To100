# Author: Tanishq Tripathi
# Date: 19/06/2025

a = 10  # Integer
b = 3.14  # Float
c = complex(2, 3)  # Complex number
d = "Hello"  # String   
e = True  # Boolean
f = None  # NoneType   
g = [1, 2, 3]  # List is mutable data type ordered collection in Python
h = (4, 5, 6)  # Tuple is immutable data type ordered collection in Python
i = {7, 8, 9}  # Set is an unordered collection of unique elements
j = {"key": "value"}  # Dictionary is a collection of key-value pairs
k = bytearray(5)  # Bytearray is a mutable sequence of bytes used to store binary data and is mutable
l = bytes(5)  # Bytes is an immutable sequence of bytes used to store binary data and is immutable different from bytearray as it cannot be modified after creation
m = memoryview(bytes(5))  # Memoryview is a view of the memory of a bytes object used to access the bytes without copying them
n = range(10)  # Range
o = frozenset([10, 20, 30])  # Frozenset is an immutable version of a set used to store unique elements and is unordered
# Printing the types of the variables
print(a)  # <class 'int'>
print(b)  # <class 'float'>
print(c)  # <class 'complex'>
print(d)  # <class 'str'>
print(e)  # <class 'bool'>
print(f)  # <class 'NoneType'>
print(g)  # <class 'list'>
print(h)  # <class 'tuple'>
print(i)  # <class 'set'>
print(j)  # <class 'dict'>
print(k)  # <class 'bytearray'>
print(l)  # <class 'bytes'>
print(m)  # <class 'memoryview'>
print(n)  # <class 'range'>
print(o)  # <class 'frozenset'>
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
