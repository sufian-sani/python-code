a=set(map(int, input().split()))
n=int(input())
count=True
for _ in range(n):
    a1 = set(map(int, input().split()))
    if len(a) > len(a1):
        if not a.issuperset(a1):
            count=False

print(count)

