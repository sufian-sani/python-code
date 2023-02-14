def check(n1,n2):
    sum=n1+n2
    if sum>=15 and sum<=20:
        return 20
    else:
        return sum

n1=int(input())
n2=int(input())
print(check(n1,n2))