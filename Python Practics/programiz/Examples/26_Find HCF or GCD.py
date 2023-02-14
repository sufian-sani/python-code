x = 54
y = 24

if x>y:
    smaller=y
else:
    smaller=x
for i in range(1,smaller-1):
    if x%i==0 and y%i==0:
        result=i

print(result)