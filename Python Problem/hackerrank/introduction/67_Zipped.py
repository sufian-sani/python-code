a = list(map(int,input().split()))
b = [map(float,input().split()) for i in range(a[1])]

for i in zip(*b):
    print(sum(i)/a[1])
