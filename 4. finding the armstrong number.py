#Finding the armstrong number
#The sum of the 3rd power of the digits in
#the Armstrong number is equal to that number.

#Entering the 3-digits number
num = int(input("Please, enter 3-digits number:"))
first_digit = num//100
second_digit = (num - first_digit*100)//10
third_digit = num%10

#Finding the armstrong number and printing the output
if num == first_digit**3 + second_digit**3 + third_digit**3:
    print("{0:d} is a armstrong number.".format(num))
else:
    print("{0:d} is not a armstrong number.".format(num))
    
