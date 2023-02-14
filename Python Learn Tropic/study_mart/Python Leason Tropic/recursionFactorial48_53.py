def myfact(x):
    if x==0:
        return 1
    return x*myfact(x-1)
result = myfact(int(input("Enter Value: ")))
print('Result: ',result)