#Reverse the number

#Entering the number
num = input("Please, enter the number")
new_list = []
for i in range(len(num)):
    new_list.append(num[i])

#Reversing the number and printing the output
new_list.reverse()
for i in range(len(new_list)):
    print(new_list[i], end='')


