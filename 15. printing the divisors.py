#Print the divisors of the number in ascending order

#Enter the number
num = int(input("Please, enter the number:"))

#Finding the divisors and printing the output
for divisors in range(1, num+1):
    if num%divisors == 0:
        print("{0:d} is the divisor of {1:d}".format(divisors, num))
