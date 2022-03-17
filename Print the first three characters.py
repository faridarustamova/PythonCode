#Print a string made of the first three characters of a specified string


def first_three(new_str):
    if len(new_str) >= 3:
        print(new_str[0] +new_str[1] +new_str[2])
    else:
        print(new_str)

first_three(input("Please, enter the string"))
