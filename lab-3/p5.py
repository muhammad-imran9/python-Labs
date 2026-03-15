'''
Write a program that will take three sides of the triangle as input and will display the area of the 
triangle at the output using hero's formula. If a, b and c are sides of triangle, area of the triangle is:  

Area = √𝑠(s - a)(a - b)(s - c)
where  s = (a + b + c)/2
We will assume that user will enter the sides of valid triangle. A triangle is valid if sum of any of its 
two sides is greater than the third side. Later, we will see how to handle the case if entered triangle 
is invalid. 


Sample output is: 
Enter the three sides of triangle (separated by commas): 4,3,2
the area of entered triangle is:  2.9047375096555625

'''

from math import *

a,b,c=eval(input("Enter the three sides of triangle (separated by commas): "))

s=(a+b+c)/2
area=sqrt(s*(s-a)*(s-b)*(s-c))

print("the area of entered triangle is:  ",area)

