def get_max_occuring_char(str1):
    ASCII_SIZE = 256
    ctr = [0] * ASCII_SIZE
    print(ctr)
    max = -1
    ch = ''
    for i in str1:
        ctr[ord(i)] += 1

    for i in str1:
        if max < ctr[ord(i)]:
            max = ctr[ord(i)]
            ch = i
    return ch

print(get_max_occuring_char("Python: Get file creation and modification date/times"))

'''
def get_max_occuring_char(str1):
    count=0
    ls_count=[]
    for i in range(len(str1)):
        for j in str1:
            if str1[i]==j:
                count+=1
        ls_count.append(count)
        count=0
    max_item=max(ls_count)
    for index,item in enumerate(ls_count):
        if max_item==item:
            return str1[index]

print(get_max_occuring_char("welcome to w3resource"))
print(get_max_occuring_char("Python: Get file creation and modification date/times"))
print(get_max_occuring_char("abcdefghijkb"))
'''

