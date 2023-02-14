def addsum(n1,n2,n3):
    if n1==n2 or n3==n2 or n1==n3:
        return 0
    else:
        sum=n1+n2+n3
    return sum

n1=int(input())
n2=int(input())
n3=int(input())

print(addsum(n1,n2,n3))

