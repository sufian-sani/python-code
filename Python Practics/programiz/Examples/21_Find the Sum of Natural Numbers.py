num=int(input('Enter a number: '))

if num < 0:
    print('error')
else:
    sum = 0
    while num > 0:
        sum+=num
        num-=1
    print(sum)