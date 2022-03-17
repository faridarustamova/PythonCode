#Adding "ing" to the end of the string. 
#If the string ends with "ing" then add "ly"
#If the lenght of string is the less than 3 leave it unchanged

#Entering the string
str1 = input("Please, enter the string:")

#Adding "ing" and printing the output
if len(str1) >=3:
    if str1[-3] == "i" and str1[-2] == "n" and str1[-1] == "g":
        str1 = str1 + "ly"
        print(str1)
    else:
        str1 = str1 + "ing"
        print(str1)
else:
    print(str1)