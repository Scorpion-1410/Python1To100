'''
Author: Tanishq Tripathi
Date: 19/06/2025
This script demonstrates basic string operations in Python, including string slicing and indexing.
'''
Names = "Tanishq, Asthana, Abhay, Nitesh" # A string variable containing names separated by commas
fruit = "Mango" 

print('the first seven characters from name string:',Names[0:7]) # Printing the first seven characters from the name string
print('the characters from the eighth to the twelfth character:', Names[9:16]) # Printing the characters from the eighth to the sixteenth character
print('the length of the name string:',len(fruit)) # Printing the length of the fruit string
print('the entire string from the ninth character:', Names[9:]) # Printing the entire string from the ninth character
print('the first three characters of my name:', Names[:3]) # Printing the first three characters of my name 
print('the first two characters of the fruit string:',fruit[0:-3]) # Printing the first two characters of the fruit string fruit[0:len(fruit)-3]
print('the characters from the third to the fourth character:', fruit[-3:-1]) # Printing the characters from the third to the fourth character from fuit string fruit[len(fruit)-3:len(fruit)-1]
print('the last character of my name:', Names[-1]) # Printing the last character of my name

nm = 'Fruit'
print(len(nm)) # Printing the length of the nm string
print(nm[-4:-2]) # Printing the characters from the second to the third character from nm string nm[1:3]