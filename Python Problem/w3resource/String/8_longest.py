def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0],word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])


'''
def find_longest_word(ls):
    str=''
    max=len(ls[0])
    for i in range(len(ls)):
        sort_list = len(ls[i])
        if max<sort_list:
            max=sort_list
            str=ls[i]

    return str
        # print(i,sort_list)

ls=["PHP", "Exercises", "Backend","hjhdjdgsjgfjdsgj","uytrrddj"]
result = find_longest_word(ls)
print(result)
'''