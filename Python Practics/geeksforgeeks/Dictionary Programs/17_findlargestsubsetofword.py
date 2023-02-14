from collections import Counter
input = 'ant magenta magnate tan gnamate'
input=input.split(" ")
for i in range(0,len(input)):
    input[i]=''.join(sorted(input[i]))

freqDict = Counter(input)

print(max(freqDict.values()))