n=int(input("Enter a number:"))

for i in range(2,n+1):
    if n%i==0:
        print(i)
        break
    else:
        pass
