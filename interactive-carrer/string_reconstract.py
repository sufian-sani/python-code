def find_char(str):
    str_char = ''
    for ch in str:
        if ch.isalpha():
            str_char += ch
    return str_char


str = input()
print(find_char(str))
