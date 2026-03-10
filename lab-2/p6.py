"""
Write a program to find the area and volume of the sphere from its radius. The formulas of area 
and volume of sphere are: 𝐴 = 4𝜋𝑟2 and 𝑉 = 4/3𝜋𝑟3

Sample output is:  
This program calculates area and volume of the sphere. 
Enter the radius: 4 
Area of the sphere is A: 201.14285714285714 
Volume of the sphere is V: 268.1904761904762 
"""

PI = 3.14
radius=eval(input("Enter the radius: "))
area=4*PI*radius**2
volume=(4/3)*PI*radius**3
print("Area of the sphere is A:",area)
print("Volume of the sphere is V:",volume)

