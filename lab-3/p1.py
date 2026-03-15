'''
Write a program that will take two integers as input and will display first integer as a percentage 
of other. 
Sample output is: 
Enter 1st integer: 20 
Enter 2nd integer: 30 
20 is 66.66666666666666% of 30.
'''

num1=eval(input("Enter 1st integer: "))
num2=eval(input("Enter 2nd integer: "))
percentage=num1/num2*100
print(f"{num1} is {percentage} of {num2}")
