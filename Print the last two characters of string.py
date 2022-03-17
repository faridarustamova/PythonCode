#Print the last two characters of string 4 times

#Writing a fuction to print last two characters 4 times
def last_two(new_str):
    for i in range(4):
        last_two = new_str[-2] + new_str[-1]
        print(last_two, end="")

last_two(input("Please, enter the string:"))
