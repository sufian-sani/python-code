def FibRecurs(n):
    if n<=1:
        return n
    else:
        return FibRecurs(n-1)+FibRecurs(n-2)


n=int(input())
print(FibRecurs(n))