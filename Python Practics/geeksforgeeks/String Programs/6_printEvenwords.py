s = "This is a python language"

s_s=s.split(' ')

for word in s_s:
    if len(word)%2==0:
        print(word)