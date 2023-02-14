T = int(input().strip())

L = []
for t in range(T):
    args = input().strip().split(" ")
    if args[0] == "append":
        L.append(int(args[1]))
    elif args[0] == "insert":
        L.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        L.remove(int(args[1]))
    elif args[0] == "pop":
        L.pop()
    elif args[0] == "sort":
        L.sort()
    elif args[0] == "reverse":
        L.reverse()
    elif args[0] == "print":
        print(L)

'''
N = int(input())
list=[]
list.append(N)
list.append(int(input()))
list.append(int(input()))
list.pop(0)
rev_num=int(input())
list.insert(0,rev_num)
print(list)
list.remove(rev_num)
list.append(int(input()))
list.append(int(input()))
list.sort()
print(list)
list.pop()
list.reverse()
print(list)
'''