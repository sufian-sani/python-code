string_1=input('Take a string 1: ')
string_2=input('Take a string 2: ')

string_1=list(string_1)
string_2=list(string_2)

string_1=set(string_1)
string_2=set(string_2)

cl=string_1.union(string_2)

for i in cl:
    print(i)

'''
s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
a=list(set(s1)|set(s2))
print("The letters are:")
for i in a:
    print(i)
'''