patterns = ['ape', 'apple', 'peach', 'puppy']

i_put='appel'
i_set=set(i_put)
count=0
for i in patterns:
    c_set=set(i)
    inter=i_set.intersection(c_set)
    for j in range(len(inter)):
        if j>=2:
            print(i)
            break
        else:
            pass
