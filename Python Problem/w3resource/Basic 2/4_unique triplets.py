# def three_sum(nums):
#   result = []
#   nums.sort()
#   for i in range(len(nums)-2):
#     if i> 0 and nums[i] == nums[i-1]:
#       continue
#     l, r = i+1, len(nums)-1
#     while l < r:
#       s = nums[i] + nums[l] + nums[r]
#       if s > 0:
#         r -= 1
#       elif s < 0:
#           l += 1
#       else:
#         # found three sum
#         result.append((nums[i], nums[l], nums[r]))
#         # remove duplicates
#         while l < r and nums[l] == nums[l+1]:
#           l+=1
#           while l < r and nums[r] == nums[r-1]:
#             r -= 1
#             l += 1
#             r -= 1
#           return result
#
# x = [1, 1, -2, 1, -2, 0, -6, 1, 2]
# print(three_sum(x))


def uniquetriple(ls):
    lenth=len(ls)-3
    for i in range(lenth):
        if ls[i]+ls[i+1]+ls[i+2]==0:
            return ls[i], ls[i + 1], ls[i + 2]

# ls=[1, -1, 2, 0, -2, 0, -6, 4, 2]
ls=[1, 1, -2, 1, -2, 0, -6, 1, 2]
print(uniquetriple(ls))