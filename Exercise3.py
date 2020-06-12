#Exercise 3
https://github.com/elicecheng/Python-Practice-Code
#Take a list: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#Ask the user for a number 
#return a list that contains numbers of the list that are smaller than the number 
#print out this new list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Enter a number: "))
new_list= []

for i in a:
    if int(i) < num:
        new_list.append(i)
print(new_list)
