from itertools import groupby

args = input().strip()

for key, group in groupby(args):
    print((len(list(group)),int(key)),end=' ')
    # print((len(list(group)), int(key)), end=" ")

# for key, group in groupby(args):
#     print((len(list(group)), int(key)), end=" ")