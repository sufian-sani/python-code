s = "GeeksforGeeks"
d=2

l_side=s[d:]
l_sideAdd=s[:d]

r_side=s[:len(s)-d]
r_sideAdd=s[len(s)-d:]

print('Left side Rotation:',l_side+l_sideAdd)
print('Right side Rotation:',r_sideAdd+r_side)