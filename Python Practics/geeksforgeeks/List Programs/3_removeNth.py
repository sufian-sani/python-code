def RemoveIthWord(list, word, N):
    count = 0

    for i in range(0, len(list)):
        if (list[i] == word):
            count = count + 1

            if (count == N):
                del (list[i])
                return True

    return False

list = ['geeks', 'for', 'geeks']
word = 'geeks'
N = 1

flag = RemoveIthWord(list, word, N)

if (flag == True):
    print("Updated list is: ", list)
else:
    print("Item not Updated")