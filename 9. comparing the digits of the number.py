#Checking if digits of the number different from each other

#Entering the number
num = input("Please, enter the 4-digits number:")

#Cheching the digits of the number
if int(num[0]) != int(num[1]) != int(num[2]) != int(num[3]):
    print("YES")
else:
    print("NO")
