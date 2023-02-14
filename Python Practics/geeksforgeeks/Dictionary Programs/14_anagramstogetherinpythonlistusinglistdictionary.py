# Function to return all anagrams together
input = ['cat', 'dog', 'tac', 'god', 'act']

dict = {}

for strVal in input:
    key = ''.join(sorted(strVal))
    if key in dict.keys():
        dict[key].append(strVal)
    else:
        dict[key] = []
        dict[key].append(strVal)
    output = ""
    for key, value in dict.items():
        output = output + ' '.join(value) + ' '

print(output)