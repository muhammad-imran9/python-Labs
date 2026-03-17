'''
Write a program that will take two numbers as input (say a and b) and will show their ratio at 
output (a/b). As you know that division by zero is not possible and a run-time error occurs in an 
attempt to divide by zero. You have to incorporate this problem in a way that if second number 
entered is zero, program should not calculate the ratio; instead it should display a message that 
division by zero is not possible. 


Sample output is: 
Enter first number: 5 
Enter second number: 2 
Ratio of two numbers is: 2.5 


Another sample output is: 
Enter first number: 16 
Enter second number: 0 
Division by zero is not possible! 

'''


# input two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# check for division by zero
if b == 0:
    print("Division by zero is not possible!")
else:
    ratio = a / b
    print("Ratio of two numbers is:", ratio)