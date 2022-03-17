#Choose the longest word in the whole string

#Coosing the longest word and printing the ouput
def longestWord(new_str):
    lst = new_str.split()
    length = []
    for i in range(len(lst)):
        length.append(len(lst[i]))
    print(max(length))

longestWord(input("Please, enter the list of words:"))