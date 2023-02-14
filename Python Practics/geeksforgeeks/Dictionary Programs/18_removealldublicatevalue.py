from collections import Counter
input = 'Geeks for Geeks'

input=input.split(" ")
for i in range(0,len(input)):
    input[i]=''.join(sorted(input[i]))

UniqW = Counter(input)
print(UniqW)

s = " ".join(UniqW.keys())
print(s)