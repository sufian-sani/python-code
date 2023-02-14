def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            print('if part total:',total)
            print('if part element:',element)
            total = total + sum1(element)
        else:
            print('else part total:',total)
            print('else part element:',element)
            total = total + element
    return total
print( "Sum is:",sum1([[1,2],[3,4]]))


























'''
def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum1(element)
        else:
            total = total + element
    return total
print( "Sum is:",sum1([[1,2],[3,4]]))
'''