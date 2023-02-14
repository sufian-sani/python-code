# def frequency_check(str):
#     dict={}
#     for n in str:
#         keys=dict.keys()
#         if n in keys:
#             dict[n]+=1
#         else:
#             dict[n]=1
#
#     return dict
#
# str='google.com'
# print(frequency_check(str))

# str='google.com'

dict={'g':8,'f':4}

m=max(dict.values())

for keys,values in dict.items():
    if values==m:
        print(keys)
