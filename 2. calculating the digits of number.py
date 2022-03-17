#Calculating the sum and times of the digits of the number

#Entering the number
num = input("Please, enter an integer:")

#Calculating the output
sum1 = 0
times = 1
for i  in range(len(num)):
    sum1 = sum1 + int(num[i])
    times = times * int(num[i])
print("This number {1:d} sum of digits is {0:d} ".format(sum1, int(num)))
print("This number {1:d} times of digits is {0:d} ".format(times, int(num)))
