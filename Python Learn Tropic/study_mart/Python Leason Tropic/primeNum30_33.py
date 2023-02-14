num = int(input('Enter any integer number: '))

for i in range(2,num):
    if num % i == 0:
        print('Not a Prime Number')
        break
else:
    print('Oh! it\'s a Prime Number.')