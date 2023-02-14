'''
def check(ls):
    ls_up=[]
    count=0
    for i in ls:
        for j in range(len(ls)):
            if i==ls[j]:
                count+=1
        ls_up.append(count)
        count=0
    if 2 in ls_up:
        return False
    else:
        return True
'''
def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;

# ls=[2,4,5,7,9,5]
ls=[2,4,5,7,9]
print(test_distinct(ls))