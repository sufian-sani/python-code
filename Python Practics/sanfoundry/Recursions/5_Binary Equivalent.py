ls=[]
def binary(n1):
    if n1 == 0:
        return 1
    dig=n1%2
    ls.append(dig)
    binary(n1//2)
    return ls


n1=int(input('Take first number: '))
binary(n1)
ls.reverse()
for i in ls:
    print(i,end=' ')
























'''
l=[]
def convert(b):
    if b==0:
        return 1
    dig=b%2
    l.append(dig)
    convert(b//2)
a = int(input("Enter a number: "))
convert(a)
l.reverse()
for i in l:
    print(i,end=' ')
'''
