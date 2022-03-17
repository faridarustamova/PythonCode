#Count the occurrences of each word in a given sentence

#Entering the string
new_str = input("Please, enter the string:")

#Converting string to dictionary
lst = new_str.split()
new_dict = {}
for i in range(len(lst)):
    if lst[i] not in new_dict:
        new_dict[lst[i]] = 1
    else:
        new_dict[lst[i]]+=1

#Printing the output
for key, value in new_dict.items():
    print("the number of \'{0:s}\' is {1:d} in the string".format(key, value))