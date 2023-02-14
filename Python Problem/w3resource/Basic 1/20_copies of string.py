def filt(str,num):
    result = ""
    for i in range(num):
        result = result + str
    return result

str=input()
num=int(input())

print(filt(str,num))

'''
str='abc'
n=2
result=""
for i in range(n):
    result=result+str

print(result)
'''