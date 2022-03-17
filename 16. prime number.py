#Checking if the number is prime number

#Entering the number
num = int(input("Please, enter the number:"))
isPrime=True

#Checking the number and printing the output
for i in range(2, num):
    if num%i==0:
        print("No, it is not prime.")
        isPrime=False
        break
if isPrime:
    print("Yes, it is prime.")
        
