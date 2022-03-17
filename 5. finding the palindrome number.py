#Finding the palindrome number
#Integers are considered to be a palindrome
#when they are read in the same way from left to right and vice versa

#Entering the number
num = input("Please, enter the 4-digits number:")
first_digit = int(num[0])
second_digit = int(num[1])
third_digit = int(num[2])
fourth_digit = int(num[3])

#Finding the palindrome number and printing the output
if first_digit==fourth_digit and second_digit==third_digit:
    print("{0:d} is a palindrome number.".format(int(num)))
else:
    print("{0:d} is not a palindrome number.".format(int(num)))
