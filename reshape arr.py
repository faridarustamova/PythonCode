import numpy as np

#Entering 9 characters
new_arr = input()

#Changing the string to the string list
lst = new_arr.split()

#Changing the string list to integer list
int_lst=[]
for i in range(len(lst)):
    int_lst.append(int(lst[i]))

#Changing integer list to numpy array
my_array = np.array(int_lst)

#Changing the shape of numpy array to 3x3
new_shape = np.reshape(my_array,(3,3))
print("3x3 array:", new_shape)

