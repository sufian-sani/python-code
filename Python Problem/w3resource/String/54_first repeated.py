def first_repeated_char_smallest_distance(str1):
  temp = {}
  for ch in str1:
    if ch in temp:
      return ch, str1.index(ch)
    else:
      temp[ch] = 0
  return 'None'
print(first_repeated_char_smallest_distance("abcabc"))
print(first_repeated_char_smallest_distance("abcb"))
print(first_repeated_char_smallest_distance("abcc"))
print(first_repeated_char_smallest_distance("abcxxy"))
print(first_repeated_char_smallest_distance("abc"))


# def first_repeated_char_smallest_distance(str1):
#     f_letter=0
#     for index,c in enumerate(str1):
#         if str1[:index+1].count(c) > 1:
#             f_letter=c
#             break
#     for i in range(len(str1)):
#         if f_letter==str1[i]:
#             return f_letter,i
#     return None
#
# print(first_repeated_char_smallest_distance("abcabc"))
# print(first_repeated_char_smallest_distance("abcb"))
# print(first_repeated_char_smallest_distance("abcc"))
# print(first_repeated_char_smallest_distance("abcxxy"))
# print(first_repeated_char_smallest_distance("abc"))