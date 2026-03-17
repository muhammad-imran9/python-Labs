'''

Write a program that asks the user to enter a length in centimeters. If the user enters a negative 
length, the program should tell the user that the entry is invalid. Otherwise, the program should 
convert the length to inches and print out the result. There are 2.54 centimeters in an inch

'''


len_in_centimeter=eval(input("Enter length in centimerer: "))
if(len_in_centimeter<0):
    while(len_in_centimeter<0):
        print("Entry is invalid")
        len_in_centimeter=eval(input("Enter length in centimerer"))
        if(len_in_centimeter>0):
            break;

inches=len_in_centimeter/2.54
    

print(f'There are {inches} inches in {len_in_centimeter} length of centimeter ')
