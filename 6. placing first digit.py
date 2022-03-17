#Placing first digit to last

#Entering the number
num = int(input("Please, enter 3 digits number:"))

#Placing first digit
first_digit = num//100
last_two_digits = num%100
new_num = last_two_digits*10 + first_digit

#Printing the output
print(new_num)
