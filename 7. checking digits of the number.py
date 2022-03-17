#Checking if the number can divided by its digits

#Entering the number
num = input("Please, enter 4-digits number:")
first_digit = int(num[0])
second_digit = int(num[1])
third_digit = int(num[2])
fourth_digit = int(num[3])

#Checking the number and printing the output
if first_digit == 0 or second_digit == 0 or third_digit == 0 or fourth_digit == 0:
    print("your number has zeros, that is why you write without zero")
else:
    if int(num) % first_digit == 0 and int(num) % second_digit == 0 and int(num) % third_digit == 0 and int(num) % fourth_digit == 0:
        print("{0:d} is a wanted number".format(int(num)))
    else:
        print("{0:d} is not a wanted number".format(int(num)))
        
