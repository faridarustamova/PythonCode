#Check if the given number is palindrome or not
#The palindrome number is the number that can be read
#the same from left to right and vice versa

#Entering the number
num = input("Please, enter the number:")

#Checking the number
first_chck_dig = 0
sec_chck_dig = len(num)-1
new_num = ''
for i in range(len(num)//2):
    if num[first_chck_dig] == num[sec_chck_dig]:
        first_chck_dig = first_chck_dig +1
        sec_chck_dig = sec_chck_dig - 1
        new_num = num

#Printing the output
if new_num == num:
    print("Yes")
else:
    print("No")


        

