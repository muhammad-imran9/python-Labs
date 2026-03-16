'''

Write a program that will take input a vector (in form of complex number) from user and will 
display the unit vector (in form of complex number) of that. 
Use proper number formatting so that only two digits after decimal points are displayed. 


Sample output is: 
Enter a Vector (in the form of Complex Number): 2-3j 
The Unit vector of entered vector is:  
(0.55-0.83j) 

'''

from math import *

vector=complex(input("Enter a Vector (in the form of Complex Number): "))
magnitute=sqrt((    ((vector.real)**2)  +  ((vector.imag)**2)    ))


print(f'The Unit vector of entered vector is: \n ( {vector.real/magnitute}  {vector.imag/magnitute} )' )
