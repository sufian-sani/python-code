# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)


'''
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

ip_str=ip_str.casefold()

vowels_dict={}

for i in vowels:
    count=ip_str.count(i)
    vowels_dict[i]=count

print(vowels_dict)
'''
'''-----------------'''
'''
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

list_ip_str=list(ip_str)
list_ip_str_len=len(list_ip_str)

ip_str=ip_str.casefold()
value=0
result_vowels=[]
result_counter=[]

for i in ip_str:
    if i in vowels:
        for j in range(1,list_ip_str_len):
            if i in result_vowels:
                pass
            elif i==list_ip_str[j]:
                value=value+1
                result_vowels.append(i)
        result_counter.append(value)
        value=0

print(result_vowels)
print(result_counter)
'''