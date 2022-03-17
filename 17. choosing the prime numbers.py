#Choosing the prime numbers less than given number 

#Entering the number
num = int(input("Please, enter the number:"))
isPrime=True

#Choosing the prime numbers and printing the output
for j in range(2, num):
    isPrime=True
    for i in range(2, j):
        if j%i == 0:
            #print(j,"No, it is not prime")
            isPrime=False
            break
    if isPrime:
        print(j,"Yes, it is prime")
            
