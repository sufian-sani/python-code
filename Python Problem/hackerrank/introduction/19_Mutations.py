def mutate_string(s, i, c):
    s = s[:i] + c + s[i+1:]
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

'''
def mutate_string(string, pos, char):
    s = string[:pos] + char + string[pos+1:]
    return s

string = input('')
i = input().split()

position = 0
character = ' '
for s in i:
    if s.isdigit():
        position=s
    else:
        character=s
pos = int(position)
char = str(character)
print(mutate_string(string,pos,char))

'''
'''
mylist=['1','orange','2','3','4','apple']

for s in mylist:
    if s.isdigit():
        print(s)
    else:
        print(s)
mynewlist = [s for s in mylist if s.isdigit()]?
print(mynewlist)
'''