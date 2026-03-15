'''
Write a program that will take a floating input from the user and will display the integer and the 
fractional part separately. (Use data type casting to get the integer part and then subtract it from 
the original number to get the fractional part) 

Sample output is: 
Enter a floating number: 2.34 
Integer part is: 2 
Fractional part is: 0.33999999999999986 

Yes, there is little problem with the output that instead of 0.34, it is 0.33999999999999986 which 
is because of hardware limitation of computer. We will explore the solution for this in future.
'''

num=float(input("Enter a floating number: "))

integer_part=int(num)
fractional_part=num-int(num)

print("Integer part is ",integer_part)
print("Fractional part is: ",fractional_part)