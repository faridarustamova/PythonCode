#Finding the digit in hundredths place of the number

#Entering the number
num = int(input("Please, enter the number greater than 999:"))

#Finding the digit
finding_num = (num - (num//1000)*1000)//100

#Printing the output
print(finding_num)
