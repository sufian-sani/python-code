def inc(x):
    return x+1
def dec(x):
    return x-1

def op(func,x):
    result = func(x)
    return result

# print(inc(10))
# print(dec(10))
print(op(inc,10))