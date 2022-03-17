#Remove the characters which have odd index values of a given string

#Entering the string
new_str = input("Please, enter the string:")

#Removing the odd index values and printing the output
lst = new_str.split()
for i in range(len(lst)):
    if i%2 == 0:
        print(lst[i], end=" ")