def find_prime(n,m):
    for i in range(n,m):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

n = int(input('Enter First Value: '))
m = int(input('Enter Second Value: '))
find_prime(n,m)
