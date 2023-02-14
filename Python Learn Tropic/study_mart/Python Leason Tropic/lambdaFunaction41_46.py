'''
def mul(x,y,z):
    return x*y*z
result = mul(2,6,8)
print(result)
'''
result = (lambda x,y,z : x*y*z) (2,6,8)
print(result)