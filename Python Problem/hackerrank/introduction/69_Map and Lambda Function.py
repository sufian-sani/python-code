
cube = lambda x: x ** 3

def fibonacci(n):
    List = [0, 1]
    for i in range(2, n):
        List.append(List[i - 1] + List[i - 2])

    return (List[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

'''
cube = lambda x: x ** 3

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input())
ls=[]
for i in range(n):
    ls.append(fibonacci(i))
    # print(fibonacci(i))

# ls_int=list(map(int,ls))
# for j in ls_int:
#     print(type(j))

print(list(map(cube,ls)))
'''
