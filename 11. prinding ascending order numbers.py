#Print all the numbers that are less than the given number and are arranged in ascending order.


#Entering the number
num = input("Please, enter the number:")
new_num = 0
new_str = ''

#Checking the number
for i in range(len(num)):
    if int(num[i]) > new_num:
        new_str = new_str + num[i]
        new_num = int(num[i])

#Printing the output
if new_str == num:
    print(num)
else:
    print("{0:d} is not a wanted number".format(int(num)))
        
    
