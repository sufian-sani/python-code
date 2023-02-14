def square(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

def square_generator(nums):
    for i in nums:
        yield i*i

my_nums = square([1,2,3,4,5])
# print(my_nums)
for num in my_nums:
    print(num)