s = input().strip()
ds=s.split(' ')
cp=[]
for i in ds:
    cap=i.capitalize()
    cp.append(cap)

achStr = ' '.join(map(str, cp))
print(achStr)