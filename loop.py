'''
Author: Tanishq Tripathi
Date: 21/07/2025
This script demonstrates the use of loops in Python, including while loops, for loops, and nested loops.
'''
i = 0  # Initialize a variable i to 0
while i < 5:  # Start a while loop that continues as long as i is less than 5
    print(i, end = '')  # Print the current value of i without a newline
    if i == 1:  # Check if i is equal to 1
        print(i) # If true, print i on a new line
    i += 1  # Increment i by 1 after each iteration
print()  # Print a newline after the while loop completes

# Example of a for loop iterating over a range
for j in range(5):  # Loop through numbers from 0 to 4
    print(j, end = '')  # Print the current value of j without a newline
    if j == 1:  # Check if j is equal to 1
        print(j)  # If true, print j on a new line
print()  # Print a newline after the for loop completes

# Example of a for loop iterating over a list
fruits = ['apple', 'banana', 'cherry']  # A list of fruits 
for fruit in fruits:  # Loop through each fruit in the list
    print(fruit, end = ', ')  # Print the current fruit without a newline
print()  # Print a newline after the for loop completes

# Example of a nested loop
for i in range(3):  # Outer loop iterating from 0 to 2
    for j in range(2):  # Inner loop iterating from 0 to 1
        print(f"i: {i}, j: {j}", end = ' ')  # Print the current values of i and j without a newline
    print()  # Print a newline after each iteration of the outer loop   

# Example of a while loop with a break statement
count = 0  # Initialize a variable count to 0   
while count < 5:  # Start a while loop that continues as long as count is less than 5
    if count == 3:  # Check if count is equal to 3
        break  # If true, exit the loop
    print(count, end = ' ')  # Print the current value of count without a newline
    count += 1  # Increment count by 1 after each iteration
print()  # Print a newline after the while loop completes

# Example of a while loop with a continue statement
count = 0  # Initialize a variable count to 0   
while count < 5:  # Start a while loop that continues as long as count is less than 5
    count += 1  # Increment count by 1 at the beginning of each iteration
    if count == 3:  # Check if count is equal to 3
        continue  # If true, skip the rest of the loop and continue to the next iteration
    print(count, end = ' ')  # Print the current value of count without a newline
print()  # Print a newline after the while loop completes

# Example of a while loop with an else clause
count = 0  # Initialize a variable count to 0
while count < 5:  # Start a while loop that continues as long as count is less than 5
    print(count, end = ' ')  # Print the current value of count without a newline
    if count == 3:  # Check if count is equal to 3
        break  # If true, exit the loop including the else clause
    count += 1  # Increment count by 1 after each iteration
    
else:
    print()  # Print a newline after the while loop completes normally (not interrupted by a break)
    print("Loop completed.")  # Print a message after the while loop completes normally (not interrupted by a break)
# Example of iterating over different data structures using for loops
print("\n\n")
print("This section demonstrates how to use for loops to iterate over various data structures in Python.")

li = ["geeks", "for", "geeks"] # A list of strings
for i in li:
    print(f"List: {i}") # Print each string in the list on a new line
    
tup = ("geeks", "for", "geeks") # A tuple of strings
for i in tup:
    print(f"Tuple: {i}")
    
s = "Geeks" # A string
for i in s: 
    print(f"String: {i}")
    
d = dict({'x':123, 'y':354}) # A dictionary with key-value pairs
for i in d:
    print("%s  %d" % (i, d[i]))
    
set1 = {1, 2, 3, 4, 5, 6} # A set of integers
for i in set1:
    print(f"Set: {i}"),

# Example of a nested for loop to print a pattern
print("\n")
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

print("\n")
# Example of using an iterator to iterate through a list 
fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break
    
