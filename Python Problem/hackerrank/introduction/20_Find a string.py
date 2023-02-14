'''
def count_substring(string, sub_string):
    s = 0
    if sub_string in string:
        s = 2
    return s


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
'''

'''
string, substring = (input().strip(), input().strip())
print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))
'''

'''
S, sub = input(), input()
count = 0

while sub in S:
    i = S.find(sub)
    S = S[:i] + S[i + 1:]
    count += 1

print(count)
'''
S, sub = input(), input()
count = 0

while sub in S:
    i = S.find(sub)
    S = S[:i] + S[i + 1:]
    # print(S)
    count += 1

print(count)
