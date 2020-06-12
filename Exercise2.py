#Exercise 2

#Ask the user for a number.
#Depending on whether the number is even or odd
#print out an appropriate message to the user. 

import math
num = int(input("Enter a number: "))
sec_num = int(input("Enter another to divide by: "))

check_num = num % 2


if check_num > 0:
    print("This is a odd number.")
else:
    print("This is a even number.")

if num % sec_num == 0:
    print(num, "divides evenly by", sec_num )
else:
    print(num, "can not divide evenly by", sec_num )
