# your code goes here# Python Learn program to
# find the most occurring element
import re
from collections import Counter


def most_occr_element(word):
    # re.findall will extract all the elements
    # from the string and make a list
    arr = re.findall(r'[0-9]+', word)

    # to store maxm frequency
    maxm = 0

    # to store maxm element of most frequency
    max_elem = 0

    # counter will store all the number with
    # their frequencies
    # c = counter((55, 2), (2, 1), (3, 1), (4, 1))
    c = Counter(arr)

    # Store all the keys of counter in a list in
    # which first would we our required element
    for x in list(c.keys()):

        if c[x] >= maxm:
            maxm = c[x]
            max_elem = int(x)

    return max_elem


# Driver program
if __name__ == "__main__":
    word = 'geek4of55gee4ksabc3dr2x'
    print(most_occr_element(word))

'''
import re
from collections import Counter

word = 'geek4ofgee4ksabc3dr2x'

rex=re.compile('[0-9]+')

search=re.findall(rex,word)

count=Counter(search)

# print([x for x in count.keys()])

# count_concersion=[x for x in count.keys()]

ls=list(map(int,[x for x in count.keys()]))

max=0

max_pro=0

for x in range(len(ls)):
    if ls[x]>=max:
        max=ls[x]
        max_pro=ls[x]

print(max_pro)

'''