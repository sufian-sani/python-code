def bubble_sort(list):
    size=len(list)-1
    for i in range(size):
        for j in range(0,size-i-1):
            if list[j]>list[j+1]:
                list[j],list[j + 1]=list[j+1],list[j]
    return list


ls=list(map(int,input().split()))
print(bubble_sort(ls))