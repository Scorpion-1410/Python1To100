'''
Author: Tanishq Tripathi
Date: 20/06/2025
This script demonstrates various string methods in Python, including string manipulation, formatting, and checking properties of strings.
'''

# String are immutable in Python, meaning they cannot be changed after creation.
a = "!!!!!Tanishq!!!!!Tripathi!!!!!!Tanishq!!!!!" 
print(len(a))  # Printing the length of the string a
print(a.upper())  # Converting the string a to uppercase which will create a new string as strings are immutable
print(a.lower())  # Converting the string a to lowercase which will create a new string as strings are immutable
print(a.rstrip("!"))  # Removing any trailing characters (whitespace by default) from the string a, creating a new string
print(a.lstrip("!"))  # Removing any leading characters (whitespace by default) from the string a, creating a new string
print(a.strip("!"))  # Removing any leading and trailing characters (whitespace by default) from the string a, creating a new string
print(a.title())  # Converting the string a to title case which will create a new string as strings are immutable

print(a.replace("Tanishq", "Tani"))  # Replacing the all occurrence of "Tanishq" with "Tani" in the string a, creating a new string
heading = 'intorduction tO pYtHon.' # String is created with mixed case letters
print(heading.capitalize())  # Capitalizing the first character of the string heading, creating a new string

welcome = 'Welcome to the console'# 
print(len(welcome)) 
print(len(welcome.center(75)))
print(welcome.center(30, ".")) # if the length of provieded string is x then it will add y to it so that x + y should become 30 or y = 30 - x 


print(a.count('Tanishq'))
print(a.endswith("!")) #
print(welcome.endswith('to', 4, 10))  # Checking if the string welcome ends with 'to' between index 6 and 12
print(welcome.find('to'))  # Finding the first occurrence of 'to' in the string welcome
print(welcome.index('to'))  # Finding the first occurrence of 'to' in the string welcome, raises ValueError if not found

print(welcome.isalnum())  # Checking if the string welcome is alphanumeric (contains only letters and numbers) return false as it contains space
print(welcome.isalpha())  # Checking if the string welcome contains only alphabetic characters return false as it contains space
print(welcome.isdigit())  # Checking if the string welcome contains only digits return false as it contains letters and space
print(welcome.islower())  # Checking if the string welcome is in lowercase return false as it contains uppercase letters
print(welcome.isupper())  # Checking if the string welcome is in uppercase return false as it contains lowercase letters
print(welcome.isspace())  # Checking if the string welcome contains only whitespace characters return false as it contains letters
print(welcome.isprintable())  # Checking if the string welcome is printable (contains no non-printable characters) return true as it contains only printable characters
print(welcome.istitle())  # Checking if the string welcome is in title case (first character of each word is uppercase and the rest are lowercase) return false as it contains lowercase letters in 'to' and 'the'

print(welcome.title())  # Converting the string welcome to title case, creating a new string
print(welcome.swapcase())  # Swapping the case of each character in the string welcome, creating a new string