def selection_sort(ls):
    size=len(ls)-1
    for i in range(size):
        smallest=i
        for j in range(i+1,len(ls)):
            if ls[j]<ls[smallest]:
                smallest=j
        print(ls)
        ls[i],ls[smallest]=ls[smallest],ls[i]
    return ls

ls=list(map(int,input().split()))
print('New list: ',selection_sort(ls))