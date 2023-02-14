from math import*

a=int(input())
b=int(input())
m=int(input())

fs_ans=pow(a,b)
print(round(fs_ans))
sec_ans=fs_ans%m
print(round(sec_ans))