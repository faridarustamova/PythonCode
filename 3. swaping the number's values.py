#Swapping the values of two integer numbers

#Entering the numbers
a = int(input("Enter the value of 'a':"))
b = int(input("Enter the value of 'b':"))

#Swapping the values
#c = b - a
#b = a
#a = b + c
a,b=b,a

#Printing the output
print("the value of a = %d" % a)
print("the value of b = %d" % b)
