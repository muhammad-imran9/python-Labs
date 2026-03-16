'''
Write a program that will input a complex number and will display the magnitude of that. Do not 
use abs() function to find the magnitude; instead, get the real and imaginary part of the 
entered complex number and calculate the magnitude using this formula: 
|𝑥| = √(𝑅𝑒𝑎𝑙)2 +(𝐼𝑚𝑎𝑔)2
Use proper number formatting so that only two digits after decimal points are displayed. 

Sample Output is: 
Enter a Complex Number: 4-5j 
The magnitude of entered number is: 6.40 



Repeat task 1 but this time use the conjugate function of complex class to calculate the 
magnitude. A complex number when multiplied with its conjugate gives the square of the 
magnitude of that complex number. 
Note→ While attempting to find the square-root of the product of the number and the conjugate, 
you will get an error as sqrt() function cannot be applied to a complex number. The imaginary 
part of the product is 0 but still it is a complex number. So use the real part of the product in 
sqrt() function. 

'''


from math import *

complex_num=complex(input("Enter a Complex Number: "))
C_complex_num=complex_num.conjugate()

product=(complex_num*C_complex_num)
magnitute=sqrt(product.real)


print("The magnitude of entered number is: ",magnitute)
