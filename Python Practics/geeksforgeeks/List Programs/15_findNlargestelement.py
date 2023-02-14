def max_element(list,n):
    max_list = []
    x = len(list)

    for i in range(0,n):
        max1=0
        for j in range(x):
            if list[j] > max1:
                max1=list[j]
        max_list.append(max1)
        list.remove(max1)
    print(max_list)
        

list=[5,6,7,4,2,91,2,10]
n = 3
max_element(list,n)


'''
list=[5,6,7,4,2,91,2,10]
n = 3

list.sort()
print(list[-n:])
'''

'''
x=max(list)
max_list.append(x)
list.remove(x)
x1=max(list)
max_list.append(x1)
list.remove(x1)
x2=max(list)
max_list.append(x2)
list.remove(x2)

print(max_list)
'''