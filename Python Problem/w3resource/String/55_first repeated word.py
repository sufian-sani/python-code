def first_repeated_word(str1):
  temp = set()
  for word in str1.split():
    if word in temp:
      return word;
    else:
      temp.add(word)
  return 'None'
print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc ab ca ab bc"))
print(first_repeated_word("ab ca bc ca ab bc"))
print(first_repeated_word("ab ca bc"))


# def first_repeated_word(str1):
#     str1=list(str1.split())
#     temp={}
#     for i in str1:
#         if i in temp:
#             return i
#         else:
#             temp[i]=0
#     return None
#
# print(first_repeated_word("it have important for skill also for life"))