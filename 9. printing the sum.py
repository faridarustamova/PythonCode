#Calculating the sum of first and last to digits of 5-digits number

#Entering the number
num = int(input("Please, enter 5-digits number:"))

#Calculatinh the sum
sum1 = num//1000 + num%100

#Printing the sum
print(sum1)
