# a = "Geeks for Geeks"
# b = "Learning from Geeks for Geeks"
a="apple banana mango"
b="banana fruits mango"
a=a.split()
b=b.split()
a_set=set(a)
b_set=set(b)

e_tion=a_set.symmetric_difference(b_set)
print(e_tion)