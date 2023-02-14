def word_count(str):
    words=str.split()
    count=dict()
    for i in words:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count


print(word_count('the quick brown fox jumps over the lazy dog.'))