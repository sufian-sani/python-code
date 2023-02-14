def repert(x):
    length=len(x)
    u_list = []
    for i in range(length):
        k=i+1
        for j in range(k,length):
            if x[i] == x[j] and x[i] not in u_list:
                u_list.append(x[i])
    return u_list


list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

print(repert(list))

'''
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print(Repeat(list1))

'''