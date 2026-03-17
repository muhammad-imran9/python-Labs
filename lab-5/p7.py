'''
A perfect square is the one whose square-root is an integer e.g. 16 is perfect square and 15 is 
not. Write a program that will take a number from user and will display whether it is perfect 
square or not. 
'''

import math

# input number
num = int(input("Enter a number: "))

# find square root
root = math.sqrt(num)

# check if square root is integer
if root == int(root):
    print(num, "is a perfect square.")
else:
    print(num, "is not a perfect square.")