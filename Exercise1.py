#Exercise 1

#Asks the user to enter their name and age.
#Print out a message addressed to them that
#tells them the year that they will turn 100 years old.

import datetime

name = input("What is your name?")
age = int(input("How old are you?"))
now = datetime.datetime.now()
year = (now.year - age) + 100

print(name, "will be 100 years old in year", year)
