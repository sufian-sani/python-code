x = 54
y = 24

if x>y:
    larger=x
else:
    larger=y
while(True):
    if larger%x==0 and larger%y==0:
        result=larger
        break
    larger+=1

print(result)