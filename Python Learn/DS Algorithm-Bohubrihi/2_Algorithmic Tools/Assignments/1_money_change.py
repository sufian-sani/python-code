n=int(input())
new_n3=0
new_n2=0
new_n1=0
rest_n=0
n_c3=0
c1,c2,c3=1,5,10
while n>0:
    if n>c3:
        new_n3=n//c3
        n=n%c3
    elif n>=c2:
        new_n2=n//c2
        n=n%c2
    else:
        new_n1=n
        break
print(new_n3+new_n2+new_n1)

