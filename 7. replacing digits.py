#Replacing first digit to second

#Entering the numer
num = int(input("Please, enter 3-digit number:"))

#Replacing digits
first_digit = num//100
second_digit = (num - first_digit*100)//10
third_digit = num%10
new_num = second_digit*100 + first_digit*10 + third_digit

#Printing the output
print(new_num)
