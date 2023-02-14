def reverse_string(str):
    length=len(str)
    if length%4==0:
        str=''.join(reversed(str))
        return str
    else:
        return str


print(reverse_string('abcd'))
print(reverse_string('python'))