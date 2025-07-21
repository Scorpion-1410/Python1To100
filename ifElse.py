'''
Author: Tanishq Tripathi
Date: 21/07/2025
This script demonstrates the use of conditional statements in Python, including if-else statements, single-line if statements, and conditional expressions.
'''

age = 20  # A variable to store the age of a person

if age >= 18:  # Check if the person is 18 or older
    print("You are eligible to vote.")  # If true, print this message
else:
    print("You are not eligible to vote.") # If false, print this message
    
if age >= 18: print("You are eligible to vote.") # This is a single-line if statement that prints the message if the condition is true
else: print("You are not eligible to vote.") # This is a single-line else statement

marks = 75  # A variable to store the marks of a student

res = "Pass" if marks >= 40 else "Fail"  # A conditional expression that assigns "Pass" if marks are 40 or more, otherwise "Fail"
print(f"Result: {res}")  # Print the result of the conditional expression

age = 25 # A variable to store the age of a person for further conditional checks

if age <= 12:   # Check if the person is 12 or younger
    print("Child.") # If true, print this message
elif age <= 19: # Check if the person is between 13 and 19
    print("Teenager.") # If true, print this message
elif age <= 35: # Check if the person is between 20 and 35
    print("Young adult.") # If true, print this message
else:   # If none of the above conditions are true, the person is older than 35
    print("Adult.") # Print the final message based on the age category
    
    
# Nested if-else statement to check age and determine voting eligibility
age = 70 # A variable to store the age of a person for senior discount eligibility
is_member = True # A variable to indicate if the person is a member of a senior citizen club

if age >= 60: # Check if the person is 60 or older
    if is_member: # Check if the person is a member of a senior citizen club
        print("30% senior discount!") # If both conditions are true, print this message
    else: # If the person is 60 or older but not a member
        print("20% senior discount.") # If the person is 60 or older but not a member, print this message
else: # If the person is younger than 60
    print("Not eligible for a senior discount.") # Print this message if the person is not eligible for a senior discount

# Example of using a ternary operator for conditional assignment
senior_discount = "30% senior discount!" if (age >= 60 and is_member) else "20% senior discount." if age >= 60 else "Not eligible for a senior discount."
print(senior_discount)  # Print the result of the ternary operator

# Example of using match-case statement in Python (Python 3.10+)
# This is a more advanced feature that allows pattern matching similar to switch-case in other languages.
number = 2   # A variable to store a number for pattern matching

match number: # Start of match-case statement
    case 1: # Case for when number is 1
        print("One") 
    case 2 | 3: # Case for when number is 2 or 3
        print("Two or Three")
    case _: # Default case for any other number
        print("Other number")
a = 10  # A variable to store a number for further conditional checks
b = 20  # Another variable to store a number for further conditional checks

if a < b:  # Check if a is less than b
    pass  # If true, do nothing (pass statement) and continue with the next statement
elif a < b:  # Check if a is less than b
    print("a is less than b") 
else:  # If none of the above conditions are true
    print("a is not less than b")   # This is a simple if-else statement that checks the relationship between a and b
