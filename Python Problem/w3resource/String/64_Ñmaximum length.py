def max_consecutive_0(str1):
    return max(map(len,str1.split('1')))

str1 = '111000010000110'
print("Original string:" + str1)
print("Maximum length of consecutive 0’s:")
print(max_consecutive_0(str1))
str1 = '111000111'
print("Original string:" + str1)
print("Maximum length of consecutive 0’s:")
print(max_consecutive_0(str1))