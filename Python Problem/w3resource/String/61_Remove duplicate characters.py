from collections import OrderedDict
def remove_duplicate(str1):
    return ''.join(OrderedDict.fromkeys(str1))

print(remove_duplicate("python exercises practice solution"))
print(remove_duplicate("w3resource"))
'''
def remove_duplicate(str1):
    final_ls=[]
    final_result=''
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            if str1[i]==str1[j]:
                final_ls.append(str1[i])
    return final_ls
print(remove_duplicate("w3resource"))
'''
