pos=1
def linearsearch(ls,k):
    i=0
    while i<len(ls):
        if ls[i]==k:
            globals()[pos]=i
            return True
        i = i + 1
    else:
        return False

ls = list(map(int, input().split()))
k = int(input())

if linearsearch(ls,k):
    print('Found at',pos+1)
else:
    print('Not Found')

'''
def linearsearch(ls,k):

    for i in range(len(ls)):
        if ls[i]==k:
            return i

    return -1

ls = list(map(int, input().split()))
k = int(input())
print(linearsearch(ls,k))
'''
