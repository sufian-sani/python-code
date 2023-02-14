def remove_zeros_from_ip(str1):
    new_ip_add='.'.join([str(int(i)) for i in str1.split('.')])
    return new_ip_add
print(remove_zeros_from_ip("255.024.01.01"))