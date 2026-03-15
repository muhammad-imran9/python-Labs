'''
A Cultural Musical Concert is being held in Al-hamra Complex.  There are three seating categories in 
the hall.  Class A gallery seats cost Rs. 1000, Class B gallery seats cost Rs. 700 and Class C gallery seats 
cost Rs. 500.  Write a program that asks how many tickets for each class of seats were sold, then 
displays the amount of income generated from ticket sales.  

Sample output is: 
How many tickets sold for class A: 16  
How many tickets sold for class B: 21 
How many tickets sold for class C: 27 
Total income generated from tickets is: 44200  
'''

#constant
A=1000
B=700
C=500

#variable
classA=int(input("How many tickets sold for class A: "))
classB=int(input("How many tickets sold for class B: "))
classC=int(input("How many tickets sold for class C: "))

#calclation
income=classA*A + classB*B + classC*C

print("Total income generated from tickets is: ",income)

