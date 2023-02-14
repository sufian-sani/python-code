def check_prime(n):
    if n>0:
        for i in range(2,n):
            if (n%i)==0:
                print('It\'s not prime number')
                break
        else:
            print('It\'s a prime number')

    else:
        print('It\'s not prime number')

num = int(input('Enter The Number: '))
check_prime(num)
