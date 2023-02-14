'''
s = input()

vowels = 'AEIOU'

kevinscore = 0
stuartscore = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevinscore += (len(s)-i)
    else:
        stuartscore += (len(s)-i)

if kevinscore > stuartscore:
    print("Kevin", kevinscore)
elif kevinscore < stuartscore:
    print("Stuart", stuartscore)
else:
    print("Draw")

'''
# s = input()
s = 'BANANA'
vowels = 'AEIOU'

kevinscore = 0
stuartscore = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevinscore += (len(s)-i)
    else:
        # stuartscore += (len(s)-i)
        print(len(s)-i)
'''
s='banana'
vowel = 'aeiou'
ss=[]
sss=''
for i in s:
    if i in vowel:
        ss.append(i)
        sss=''.join(map(str,ss))
    else:
        # print(i)
        pass
print(sss)
'''