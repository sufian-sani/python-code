def check(n1,n2):
    sum=n1+n2
    sub=n1-n2
    if n1==n2:
        return True
    elif sub<=5:
        return True
    elif sum<=5:
        return True
    return False

n1=int(input())
n2=int(input())
print(check(n1,n2))