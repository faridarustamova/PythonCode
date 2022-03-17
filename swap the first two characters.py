#Get a single string from two given strings, separated by a space and swap the first two characters of each string.

#Entering the fisrt string:
str1 = input("Please, enter the first string:")

#Entering the second string:
str2 = input("Please, enter the second string:")

#Getting the new string
new_str = str2[0] + str2[1] + str1[-1] + " " + str1[0] + str1[1] + str2[-1]

#Printing the output
print(new_str)