def gcd(a,b):
    best=0
    total=a+b
    for i in range(1,total):
        if a%i==0 and b%i==0:
            best=i
    return best

a,b=map(int,input().split())
print(gcd(a,b))