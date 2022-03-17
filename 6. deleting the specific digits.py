#Delete "5" and "1" digits in the number if they have

#Entering the number
num = input("Please, enter the number:")

#Deleting "5" and "1" in the number
digits = list()
for digit in num:
    digits.append(digit)

for i in range(len(num)): 
    if '1' in digits:
        digits.remove('1')
    elif '5' in digits:   
        digits.remove('5')

#Printing the output
for i in range(len(digits)):
    print(digits[i], end="")

