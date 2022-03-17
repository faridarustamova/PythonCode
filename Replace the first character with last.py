#Replace the first character with last one in the string

#Entering the string
new_str = input("Please, enter the string:")

#Replacing the characters and printing the output
print(new_str[-1] + new_str[1:(len(new_str)-1)] + new_str[0])