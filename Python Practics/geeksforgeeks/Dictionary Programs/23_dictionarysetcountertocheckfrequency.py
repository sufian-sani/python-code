# Function to Check if frequency of all characters
# can become same by one removal
from collections import Counter

input = 'xxxxyyzz'

dict = Counter(input)

same = list(set(dict.values()))

if len(same) > 2:
    print('No')
elif len(same) == 2 and same[1] - same[0] > 1:
    print('No')
else:
    print('Yes')
