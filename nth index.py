#Remove the nth index character from a nonempty string

#Entering the string
new_str = input("Please, enter the string:")

#Entering the index 
new_index = int(input("Please, enter the index:"))

#Finding the nth index character and printing the output
print(new_str.split()[new_index])
