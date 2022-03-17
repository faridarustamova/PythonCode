#Check if the number is the exponent of 2

#Entering the number
num = int(input("Please, enter the number:"))
num1=num
exponent = 0
while num % 2 == 0:
    num = num / 2
    exponent = exponent + 1
if num == 1:
    print(num1,'is the exponent of 2')
else:
    print(num1,'is not the exponent of 2')
    

