'''
Author: Tanishq Tripathi
Date: 19/06/2025
This script demonstrates basic string operations in Python, including string creation, indexings, and iteration.
'''

mySelf = "Tanishq" # My name
friend1 = "Asthana" # My friend's name
friend2 = 'Abhay' # Another friend's name in single quotes
text1 = "He said, \"I want to eat an apple\" ." # A string variable with escaped quotes
text2 = 'He said, "I want to eat an apple" .' # A string variable with double quotes without escaped quotes
text3 = '''Hey Tanishq!.
How are you.
From where are you working these days.''' # A multi-line string variable

print("My name is", mySelf) # Printing my name
print('a string with double quotes with escaped quotes:', text1) # Printing a string with double quotes with escaped quotes
print('a string with double quotes without escaped quotes:', text2) # Printing a string with double quotes without escaped quotes
print('a multi-line string:',text3) # Printing a multi-line string
print('the first character of my name:',mySelf[0]) # Printing the first character of my name
# print(mySelf[7]) # error: IndexError: string index out of range, as my name has only 7 characters

for character in mySelf: # Iterating through each character in my name
    print('each character in my name through Iterating:',character) # Printing each character in my name
print('the length of my name is:', len(mySelf)) # Printing the length of my name
