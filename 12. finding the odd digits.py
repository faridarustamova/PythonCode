#Find the number of the odd digits in the number

#Entering the number
num = input("Please, enter the number:")

#Finding odd digits
odd_nums = ""
for digits in num:
    if int(digits)%2 != 0:
        odd_nums = odd_nums + digits

#Printing the output
print("The number of the odd digits in {0:d} is {1:d}".format(int(num), len(odd_nums)))

