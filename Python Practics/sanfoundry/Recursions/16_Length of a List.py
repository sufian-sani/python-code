def length(lst):
    if not lst:
        return 0
    print(lst)
    return 1 + length(lst[1::2]) + length(lst[2::2])
a=[5,8,7,4,2]
print("Length of the string is: ")
print(length(a))
# print(a[2::2])
























'''
def length(lst):
    if not lst:
        return 0
    return 1+length(lst[1::2]) + length(lst[2::2])

a=[1,2,3,4,5,6,9,87,23,45,69]
print("Length of the string is: ")
print(length(a))
'''