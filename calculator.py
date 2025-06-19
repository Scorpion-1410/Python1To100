print(15+6) # Addition
print(15-6) # Subtraction
print(15*6) # Multiplication
print(15/6) # Division
print(15//6) # Floor Division will give the quotient without the decimal part
print(15%6) # Modulus will give the remainder
print(2**3) # Exponentiation will give the power of the number, here 2 raised to the power of 3
print(2**-3) # Negative exponentiation will give the reciprocal of the number raised to the power, here 2 raised to the power of -3 is 1/(2**3)
print(5+2*3) # Operator precedence is followed, so multiplication is done first, then addition
print((5+2)*3) # Parentheses are used to change the order of operations
print(5+2*3-4/2) # Operator precedence is followed, so multiplication and division are done first, then addition and subtraction
print(5+2*3-4//2) # Floor division is used, so the result will be an integer
print(5+2*3-4%2) # Modulus is used, so the result will be an integer
print(5+2*3-4**2) # Exponentiation is used, so the result will be an integer
print(5+2*3-4**2//2) # Exponentiation and floor division are used, so the result will be an integer
print(5+2*3-4**2%2) # Exponentiation and modulus are used, so the result will be an integer
print(5+2*3-4**2//2%2) # Exponentiation, floor division, and modulus are used, so the result will be an integer 



a= 100
b= 10

print("The value of a is:", a)  # The value of a is: 100
print("The value of b is:", b)  # The value of b is: 10
print("The sum of", a, "and", b,"is: ", a + b)  # The sum of 100 and 10 is:  110
print("The difference of", a, "and", b, "is: ", a - b)  # The difference of 100 and 10 is:  90
print("The product of", a, "and", b, "is: ", a * b)  # The product of 100 and 10 is:  1000
print("The quotient of", a, "and", b, "is: ", a /   b)  # The quotient of 100 and 10 is:  10.0
print("The floor division of", a, "and", b, "is: ", a // b)  # The floor division of 100 and 10 is:  10
print("The modulus of", a, "and", b, "is: ", a % b)  # The modulus of 100 and 10 is:  0
# print("The exponentiation of", a, "and", b, "is: ", a ** b)  # The exponentiation of 100 and 10 is:  10000000000