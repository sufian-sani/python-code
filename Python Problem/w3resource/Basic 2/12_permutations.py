# import itertools
# # from itertools import permutations
# my_nums = [1,2,3]
#
# permutations_list=itertools.permutations(my_nums)
#
# print(list(permutations_list))

my_nums = [1,2,3]
length=len(my_nums)

for i in range(length):
    for j in range(length):
        if my_nums[i]!=my_nums[j]:
            for k in range(length):
                if my_nums[k]!=my_nums[i] and my_nums[k]!=my_nums[j]:
                    print(f'{my_nums[i]},{my_nums[j]},{my_nums[k]}')