def find_big(ls):
    max=0
    max_2=0
    for i in ls:
        if max<i:
            max=i
        else:
            pass
    return max_2

ls=[4,5,9,8,7,5,6,2,3,1,5,7,8,0,1,4,7,78,96,54,7,12,88,101]

print(find_big(ls))