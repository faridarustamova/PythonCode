#Get a string made of the first 2 and the last 2 chars from a given a string

#Entering the string
str1 = input("Please, enter the string:")

if len(str1) >= 2:
    new_str = str1[0] + str1[1] + str1[-2] + str1[-1]
    print(new_str)
else:
    print("Empty String")


