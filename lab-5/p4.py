'''
 12-Hour and 24-Hour Format 
Write a program that asks the user for an hour between 1 and 12, and then asks them to enter 
am or pm. The program then shows the hour in 24-Hour format. 
Before you proceed for the logic it is important to understand the 12:00 Noon confusion. Is it 
12am or 12pm at noon? Generally, we consider 12:00pm as noon and 12:00am as midnight. But 
the fact is 12am and 12pm both are true for midnight and it's 12:00m for the 12:00 noon. For 
simple logic here we will assume 12:00am as 12:00 Noon and 12:00pm as 12:00 midnight. 
Therefore, if user enters am, the same hour will be in 24-hours format and otherwise i.e. for pm 
it will be entered hour plus 12. 

'''


# input hour
hour = int(input("Enter hour (1-12): "))

# input am or pm
period = input("Enter am or pm: ")

# convert to 24-hour format
if period.lower() == "am":
    hour24 = hour
else:
    hour24 = hour + 12

# display result
print("Time in 24-hour format:", hour24, ":00")