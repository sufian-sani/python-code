from functools import reduce
nums = [10, 20, 30]
nums_product=reduce((lambda x,y:x*y),nums)
print(nums_product)