def sunp(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum


n=int(input("Input a number: "))
print(sunp(n))