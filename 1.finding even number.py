#Finding even number

#Entering the number
num = int(input("Please, enter the number:"))

#Choosing even number and printing the output
if num%2 == 0:
    print("{0:d} is a even number.".format(num))
else:
    print("{0:d} is a odd number.".format(num))
