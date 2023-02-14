import sys
print('Limit = ',sys.getrecursionlimit()) #recursionlimit default 1000
sys.setrecursionlimit(1500) # set recursionlimit 1500
count = 0

def Myfunction():
    global count
    count = count + 1
    print('Study Mart',count)
    Myfunction()
Myfunction()