def change_sring(str):
    first_ls=str[:1]
    last_ls=str[-1:]
    return last_ls+str[1:-1]+first_ls

print(change_sring('abcd'))
print(change_sring('abcdsgfjsgfksosunhskfh'))
print(change_sring('12345'))