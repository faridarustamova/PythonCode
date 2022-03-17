#Calculating the number of characters

#Entering the string
str1 = input("Please, enter the string:")

lst= []
dictt = {}

#Adding each character od string to list
for i in str1:
    lst.append(i)

#Creating the dictionary
for j in lst:
    if not j in dictt:
        dictt[j] = 1
    else:
        dictt[j]+=1

#Printing the output
print(dictt)