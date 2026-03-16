'''
Write a program that will ask user for the number of seconds and will print out that time in 
MM:SS format i.e. Minutes:Seconds 


Sample Output is: 
Enter Seconds: 3680 
61 : 20 

'''

seconds=int(input("Enter Seconds: "))

minute=int(seconds/60)
second=seconds%60

print(f'{minute} : {second}')