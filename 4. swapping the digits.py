#Swapping the places of the digits in 2-digit numbers

#Entering the number
num = int(input("Please, enter 2 digits number:"))

#Swapping the digits
first_digit = num//10
second_digit = num%10
new_num = second_digit*10 + first_digit

#Printing the output
print(new_num)
