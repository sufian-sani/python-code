
def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


n = int(input('Enter n: '))
print('Number of set bits:', count_set_bits(n))


# # Python3 program to Count set
# # bits in an integer
#
# # Function to get no of set bits in binary
# # representation of positive integer n */
# def countSetBits(n):
#     count = 0
#     while (n):
#         count += n & 1
#         n >>= 1
#     return count
#
#
# # Program to test function countSetBits */
# i = 9
# print(countSetBits(i))
#
# # This code is contributed by
# # Smitha Dinesh Semwal