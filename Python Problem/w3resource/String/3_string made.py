def str_made(str):
    if len(str)<2:
        return 'Empty String'
    r_str=str[:2]+str[len(str)-2:]
    return r_str

print(str_made('w3resource'))
print(str_made('w3'))
print(str_made('w'))