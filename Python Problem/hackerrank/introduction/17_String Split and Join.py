def split_and_join(a):
    s=a.split()
    s = "-".join(s)
    return s


line = input()
result = split_and_join(line)
print(result)