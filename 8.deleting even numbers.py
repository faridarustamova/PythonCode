#Deleting even numbers

#Entering the number
num = input("Please, enter 4-digits number:")

#Deleting even numbers and printing the output
for i in range(len(num)):
    if int(num[i]) % 2 != 0:
        print(num[i], end = "")
