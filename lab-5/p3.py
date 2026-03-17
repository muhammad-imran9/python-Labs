'''

Write a program that asks the user for two numbers and prints ' Entered numbers are Closed!', 
if the numbers differ within 10 units from each other and prints 'Entered numbers are Not 
Closed!' otherwise. Use if-else statement. 

Sample output is: 
Enter first number: 85 
Enter second number: 80 
Entered numbers are Closed! 


Another Sample output is: 
Enter first number: 10 
Enter second number: 80 
Entered numbers are not Closed! 



Another Sample output is: 
Enter first number: 40 
Enter second number: 45 
Entered numbers are Closed!

'''

num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))

if(     ((num1-num2)<=10)     and       ((num2-num1)<=10)):
    print("Entered numbers are Closed!")
else:
    print("Entered numbers are not Closed!")