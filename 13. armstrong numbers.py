#Finding the armstrong numbers

#Entering the number of digits
k=int(input("Please, enter the number of digits:"))

#Choosing the numbers and printing the output
for n in range(10**(k-1),10**k):
    n1=str(n)
    lst=[]
    summ=0

    for i in range(len(n1)):
        lst.append(n1[i])

    for i in lst:
        summ+=int(i)**k

    if summ==n:
        print(n,"It is Armstrong number")

