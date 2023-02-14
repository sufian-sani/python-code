def distinct_pair(ls):
    for i in ls:
        for j in range(len(ls)):
            test=i*ls[j]
            if test%2!=0:
                return True

# ls=[2, 4, 6, 8]
ls=[1, 6, 4, 7, 8]
print(distinct_pair(ls))