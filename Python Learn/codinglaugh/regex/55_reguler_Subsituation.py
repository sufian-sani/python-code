import re

a  = 'This is 1234 to 4567 haha'

# p = re.sub('\d.*','',a)
# p = re.sub('\D','',a)
# p = re.sub('\d','0',a)
p = re.sub('\d.*','0',a)

print(p)