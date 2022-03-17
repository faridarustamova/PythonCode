#Replace the smallest number with half of the sum of those numbers,
#and the largest with twice the sum of these numbers.

#Entering the numbers
x = int(input("Please, enter the value of x:"))
y = int(input("Please, enter the value of y:"))

#Cpmparing, calculating and getting new values
if x!=y:
    if x<y:
        x = (x+y)/2
        y = x*4
        print("x = {0:.2f}".format(x))
        print("y = {0:.2f}".format(y))
    else:
        y = (x+y)/2
        x = y*4
        print("y = {0:.2f}".format(y))
        print("x = {0:.2f}".format(x))
