'''
# Python3 program for removing i-th
# indexed character from a string

# Removes character at index i
def remove(string, i):
    # Characters before the i-th indexed
    # is stored in a variable a
    a = string[: i]

    # Characters after the nth indexed
    # is stored in a variable b
    b = string[i + 1:]

    # Returning string after removing
    # nth indexed character.
    return a + b


# Driver Code
if __name__ == '__main__':
    string = "geeksFORgeeks"

    # Remove nth index element
    i = 5

    # Print the new string
    print(remove(string, i))
'''

'''
str = "Geeks"
s_str = len(str)
c_list = list(str)
k=2

for i in range(2-1):
    if i==k:
        c_list.remove(c_list[i])
    else:
        c_list.append(c_list[i])
        u_str = ''.join(c_list)
print(u_str)
'''