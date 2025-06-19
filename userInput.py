'''
Author: Tanishq Tripathi
Date: 19/06/2025
This script demonstrates how to take user input in Python and perform operations on it. 
'''

a = input("Enter a Number: ")
print("You entered:", a)


x = input("Enter second Number: ")
y = input("Enter a third Number: ")


print(x + y)  # This will concatenate the strings x and y
print(int(x) + int(y))  # This will convert x and y to integers and then add them

print(x - y)  # This will raise an error because x and y are strings

print(x / y)  # This will raise an error because x and y are strings

print(x * y)  # This will raise an error because x and y are strings

print(x ** y)  # This will raise an error because x and y are strings

print(x // y)  # This will raise an error because x and y are strings