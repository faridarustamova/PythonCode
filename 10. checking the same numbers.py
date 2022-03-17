#Finding the same numbers

#Entering the numbers
num1 = int(input("Please, enter first number:"))
num2 = int(input("Please, enter second number:"))
num3 = int(input("Please, enter third number:"))

#Comparing the number and printing the output
if num1 == num2 == num3:
    print(3)
elif (num1 == num2 != num3) or (num1 == num3 != num2) or (num2 == num3 != num1):
    print(2)
else:
    print(0)
