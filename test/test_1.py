# str1='abcdef'
# print(str1[2:])

# text= 'Love thy neighbor'
#
# # splits at space
# print(text.rsplit())
#
# grocery = 'Milk, Chicken, Bread'
#
# # splits at ','
# print(grocery.rsplit(','))
#
# # Splitting at ':'
# print(grocery.rsplit(':'))

# from decimal import Decimal
# remainder = 80.remainder_near(Decimal('0.10'))
#
# print(remainder)

# def a(x):
#     yield x
#
# ls=a(455)
#
# for i in ls:
#     print(i)

# import time
# start_time = time.time()
#
# ls=[4,5,8,7,1,10,8,9,4,77,2,3,6,9,5]
#
# max=0
# i=0
# while i<len(ls):
#     if max<ls[i]:
#         max=ls[i]
#     i+=1
#
# print(max)
# print(time.time() - start_time)

# import random
#
# # print('{:d}'.format(0x0a))
# # print('{:c}'.format(65))
# print('{:06x}'.format(random.randint(0,0xFFFFFF)))

# import string
# print("Generate a random color hex:")
# print("#{:06x}".format(random.randint(0, 0xFFFFFF)))
#
# print(random.randint(0, 10) * 7)

# a=6
# b=5
# data = a & b
#
# print(data)

# result_perms = [[],[],[]]
# my_nums = [1,2,3]
# for i in result_perms:
#     print(len(i))
# print(my_nums[1:])
# ls=[]
# ls.append(my_nums)
# print(ls)

# Python program to illustrate
# *args with first extra argument
# def myFun(arg1, *argv):
# def myFun(arg1, arg2, *argv):
# 	print ("First argument :", arg1)
# 	print ("First argument :", arg2)
# 	for arg in argv:
# 		print("Next argument through *argv :", arg)
#
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# def find_max(nums):
#     max_num = float("-inf") # smaller than all other numbers
#     for num in nums:
#         if num > max_num:
#             max_num=num
#
#     return max_num
#
# # ls=[8,6,5,4,7,2,9]
# # nums=list(map(int,ls))
#
# print(find_max(nums))