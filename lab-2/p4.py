"""
Write a program that asks the user to enter a numeric value and prints both the value and the 
double of that value.

#Sample output is: 
Enter any value you want: 2.6 
You Entered: 2.6 Double of which is: 5.2 

"""


value=eval(input("Enter any value want: "))
result=value+value
print(f"You Entered: {value} Double of which is: {result} ")