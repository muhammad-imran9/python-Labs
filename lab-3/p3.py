'''
Write a program that will take a three-digit number as input and will display three digits 
separately in a column and show their sum. (At present we can assume that user is sensible 
enough to actually enter a three-digits number. Later, in coming lab sessions we will see how to 
check if user has actually entered valid input and ask to re-enter if it is invalid) 

Sample output is: 
Enter a 3-digit number: 564 
 
 5  
 6  
 4  
 
 5 + 6 + 4 = 15
'''

num=int(input("Enter a 3-digit number: "))

last_digit=num%10 
q1=int(num/10)
secondlast_digit=q1%10
first_digit=int(q1/10)


sum=first_digit+secondlast_digit+last_digit

print(first_digit)
print(secondlast_digit)
print(last_digit)


print(first_digit , " + " , secondlast_digit , " + " , last_digit , " = " , sum)