from collections import Counter

input =['john','johnny','jackie','johnny','john','jackie','jamie','jamie',
'john','johnny','jamie','johnny','john']

votes = Counter(input)

dict={}
for value in votes.values():
    dict[value] = []

for key,value in votes.items():
    dict[value].append(key)

maxVote = sorted(dict.keys(),reverse=True)[0]


if len(dict[maxVote])>1:
    print(sorted(dict[maxVote])[0])
else:
    print(dict[maxVote][0])