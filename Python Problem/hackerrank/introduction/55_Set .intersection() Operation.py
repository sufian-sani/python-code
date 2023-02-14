n = int(input())
n1 =set(map(int, input().strip().split(' ')))
b = int(input())
b1 =set(map(int, input().strip().split(' ')))

uni_set=n1.intersection(b1)

print(len(uni_set))