n=int(input('Enter any number: '))
ls=list(map(int,str(n)))
size=len(ls)
arm=0
for i in ls:
    a=i**size
    arm=arm+a

if n==arm:
    print('The number is an armstrong number.')
else:
    print('The number isn\'t an arsmtrong number.')