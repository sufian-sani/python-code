def merge_sort(ls,start,end):
    if end-start > 1:
        mid= (start+end) // 2
        print('Mid: ',mid)
        print('1st step of broke befour: ',ls,start,mid)
        merge_sort(ls,start,mid)
        print('1st step of broke after: ', ls, start, mid)
        print('2nd step of broke befour: ', ls,mid,end)
        merge_sort(ls,mid,end)
        print('2nd step of broke after: ', ls,mid,end)
        merge_list(ls, start, mid, end)
        print('Final: ',ls, start, mid, end)

def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    print('Left array:',left)
    print('Right array:',right)
    k = start
    i=0
    j=0
    print(start,mid,end)
    print('k',k)
    while start+i < mid and mid+j < end:
        if left[i] <= right[j]:
            print('k', k)
            ls[k] = left[i]
            print('1st Left: ',left[i])
            print('1st Right: ',right[j])
            print('1st i: ',i)
            print('1st j: ',j)
            i=i+1
        else:
            print('k', k)
            ls[k] = right[j]
            print('2nd Right: ',right[j])
            print('2nd Left: ',left[i])
            print('2nd i: ', i)
            print('1nd j: ', j)
            j=j+1
        k=k+1
    print(start, mid, end)
    if start+i < mid:
        while k<end:
            print('k', k)
            ls[k]=left[i]
            print('3rd Left: ',left[i])
            print('3rd i: ', i)
            i=i+1
            k=k+1

    else:
        while k<end:
            print('k', k)
            ls[k] = right[j]
            print('4th Right: ',right[j])
            print('4th j: ', j)
            j = j + 1
            k = k + 1


ls=list(map(int,input().split()))
start=0
end=len(ls)
merge_sort(ls,start,end)
print('New list: ',ls)

'''
def merge_sort(ls,start,end):
    if end-start > 1:
        mid= (start+end) // 2
        merge_sort(ls,start,mid)
        merge_sort(ls,mid,end)
        merge_list(ls, start, mid, end)

def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i=0
    j=0
    while start+i < mid and mid+j < end:
        if left[i] <= right[j]:
            ls[k] = left[i]
            i=i+1
        else:
            ls[k] = right[j]
            j=j+1
        k=k+1
    if start+i < mid:
        while k<end:
            ls[k]=left[i]
            i=i+1
            k=k+1
    else:
        while k<end:
            ls[k] = right[j]
            j = j + 1
            k = k + 1


ls=list(map(int,input().split()))
start=0
end=len(ls)
merge_sort(ls,start,end)
print('New list: ',ls)
'''