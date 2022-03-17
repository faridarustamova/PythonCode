#Delete the even digits in the number

#Entering the number
num=input("Please, enter the number:")

new_str=""
#Deleting the even digits
for digits in num:
    if int(digits) % 2 != 0:
        new_str = new_str + digits

#Printing the output
print(new_str)
