#Get a string from a given string where all occurrences of its first char 
# have been changed to '$', except the first char itself. 

#Entering the string
str1 = input("Please, enter the string:")

lst = []
lst.append(str1[0])
#Replacing character with $
for i in range(1, len(str1)):
    if str1[i] != str1[0]:
        lst.append(str1[i])
    else:
        lst.append("$")

#Printing the output
for j in range(len(lst)):
    print(lst[j], end="")