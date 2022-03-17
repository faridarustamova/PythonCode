#Digits increase from left to right on the number

#Entering the number
num = input("Please, enter the 5-digits number:")

#Cheking the number and printing the result
if int(num[0])<int(num[1])<int(num[2])<int(num[3])<int(num[4]):
    print("Yes")
else:
    print("No")
