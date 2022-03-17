#Find all the 3-digits armstrongs numbers

#Finding the armstrong number and printing the output
for num in range(100,1000):
    if num == (num//100)**3 + ((num//10)%10)**3 + (num%10)**3:
        print("{0:d} is a armstrong number.".format(num))



    
