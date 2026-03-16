'''
4] Write a program that will input a complex number and will display the magnitude of that. Do not 
use abs() function to find the magnitude; instead, get the real and imaginary part of the 
entered complex number and calculate the magnitude using this formula: 
|x| = √(Real)2 +(𝐼𝑚𝑎𝑔)2
Use proper number formatting so that only two digits after decimal points are displayed. 


Sample Output is: 
Enter a Complex Number: 4-5j 
The magnitude of entered number is: 6.40
'''

from math import *

complex_num=complex(input("Enter a Complex Number: "))

magnitute=sqrt((    ((complex_num.real)**2)  +  ((complex_num.imag)**2)    ))


print("The magnitude of entered number is: ",magnitute)
