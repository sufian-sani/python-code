def sqer(a):
    b=[]
    for i in a:
        yield(i*i)

a = sqer([1,2,3,4,5])

for num in a:
    print(num)