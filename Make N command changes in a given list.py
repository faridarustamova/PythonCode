#Make N command changes in a given list 

#Enter the number of commands
N = int(input())

#Creating empty list to make changes
new_list = list()

#Entering the commands
for i in range(N):
    cmd = input()
    if cmd.split()[0] == "insert":
        a = cmd.split()[1]
        b = cmd.split()[2]
        new_list.insert(int(a), int(b))
    elif cmd.split()[0] == "append":
        c = cmd.split()[1]
        new_list.append(int(c))
    elif cmd.split()[0] == "remove":
        d = cmd.split()[1]
        d=int(d)
        new_list.remove(d)
    elif cmd == "print":
        print(new_list)
    elif cmd == "sort":
        new_list.sort()
    elif cmd == "pop":
        new_list.pop()
    elif cmd == "reverse":
        new_list.reverse()
