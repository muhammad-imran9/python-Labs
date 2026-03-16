'''
Write a program that will ask user for the number of seconds and will print out that time in 
the format: HH:MM:SS 

Sample Output is: 
Enter Seconds: 7580 
2 : 6 : 20 

'''

seconds=int(input("Enter Seconds: "))

hour=int(seconds/3600)
minute=int((seconds%3600)/60)
second=(seconds%3600)%60

print(f'{hour} + {minute} + {second}')
