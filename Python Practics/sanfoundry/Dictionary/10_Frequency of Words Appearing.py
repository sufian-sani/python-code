string=input('Take a string: ')
l=[]
l=string.split()

wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))
