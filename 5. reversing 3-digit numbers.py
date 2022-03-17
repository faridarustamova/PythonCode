#Reversing the 3-digit numbers

#Entering number
num = int(input("Please, enter 3 digits number:"))

#reversing the number
first_digit = num//100
second_digit = (num - 100*first_digit)//10
third_digit = num%10
reversing_num = third_digit*100 + second_digit*10 + first_digit

#printing the output
print(reversing_num)
