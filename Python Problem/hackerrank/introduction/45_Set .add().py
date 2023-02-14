n=int(input())
ls=set()

for i in range(n):
    str=input()
    ls.add(str)

result=0
for j in range(len(ls)):
    result+=1
print(result)