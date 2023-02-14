l1 = []
num1 = int(input('Enter size of list 1: '))
for n in range(num1):
    numbers1 = int(input('Enter any number:'))
    l1.append(numbers1)

l2 = []
num2 = int(input('Enter size of list 2:'))
for n in range(num2):
    numbers2 = int(input('Enter any number:'))
    l2.append(numbers2)

l1_set=set(l1)
l2_set=set(l2)

inter=l1_set.intersection(l2)
print(list(inter))