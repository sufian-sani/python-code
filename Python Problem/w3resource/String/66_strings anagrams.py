def make_map(s):
    temp_map={}
    for char in s:
        if char not in temp_map:
            temp_map[char] = 1
        else:
            temp_map[char] +=1
    print(temp_map)

def make_anagram(str1,str2):
    str1_map1=make_map(str1)


str1 = "spearmk"
str2 = "pearsuv"
# str1 = input("Input string1: ")
# str2 = input("Input string2: ")
print(make_anagram(str1, str2))