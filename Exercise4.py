#Create a program that asks the user for a number 
#and then prints out a list of all the divisors of that number.
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.

num = int(input("Please enter a number: "))

numRange = list((range(1, num + 1)))

divisorList = []

for n in numRange:
  if n % num == 0
    divisorList.append(n)
print(divisorList)
