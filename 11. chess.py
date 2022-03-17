#Checking if the chess checkers are the same in colour and the horse can move

#Entering the coordinations of the chess checkers
first_num = int(input("Please, enter first number(between 1-8):"))
second_num = int(input("Please, enter second number(between 1-8):"))
third_num = int(input("Please, enter third number(between 1-8):"))
fourth_num = int(input("Please, enter fourth number(between 1-8):"))

#Checking the first colour
colour1 = ""
if first_num % 2 != 0 and second_num % 2 != 0:
    colour1 = "The first colour is black"
    print(colour1)
elif first_num % 2 == 0 and second_num % 2 != 0:
    colour1 = "The first colour is white"
    print(colour1)
elif first_num % 2 != 0 and second_num % 2 == 0:
    colour1 = "The first colour is white"
    print(colour1)
elif first_num % 2 == 0 and second_num % 2 == 0:
    colour1 = "The first colour is black"
    print(colour1)

#Checking the second colour
colour2 = ""
if third_num % 2 != 0 and fourth_num % 2 != 0:
    colour2 = "The first colour is black"
    print(colour2)
elif third_num % 2 == 0 and fourth_num % 2 != 0:
    colour2 = "The first colour is white"
    print(colour2)
elif third_num % 2 != 0 and fourth_num % 2 == 0:
    colour2 = "The first colour is white"
    print(colour2)
elif third_num % 2 == 0 and fourth_num % 2 == 0:
    colour2 = "The first colour is black"
    print(colour2)

#Checking the difference of the colours and printing the output
if colour1 == colour2:
    print("Yes")
else:
    print("No")

#Checking the move of the horse and printing the output
if (third_num - first_num == 1 and fourth_num - second_num == 2) or\
   (third_num - first_num == 2 and fourth_num - second_num == 1) or\
   (third_num - first_num == -1 and fourth_num - second_num == 2) or\
   (third_num - first_num == 2 and fourth_num - second_num == -1) or\
   (third_num - first_num == 1 and fourth_num - second_num == -2) or\
   (third_num - first_num == -2 and fourth_num - second_num == 1) or\
   (third_num - first_num == -1 and fourth_num - second_num == -2) or\
   (third_num - first_num == -2 and fourth_num - second_num == -1):
    print("Yes")
else:
    print("No")
   
