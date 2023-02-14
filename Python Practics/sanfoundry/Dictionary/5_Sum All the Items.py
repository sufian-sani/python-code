d={'A':100,'B':540,'C':239}
'''
count=0
for i in d.values():
    count=count+i

print(count)
'''
print(sum(d.values()))