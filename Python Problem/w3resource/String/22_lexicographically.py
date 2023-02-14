# def lexicographi_sort(str):
#     str=sorted(str)
#     return str
def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quickbrown'))