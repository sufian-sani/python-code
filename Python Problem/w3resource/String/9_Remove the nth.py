# def remove_char(str,n):
#     str1=''
#     for i in range(len(str)):
#         if i==n:
#             pass
#         else:
#             str1+=str[i]
#     return str1

def remove_char(str,n):
    first_part = str[:n]
    last_part = str[n+1:]
    return first_part+last_part

print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))