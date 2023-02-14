num=int(input('Enter a number: '))

# inciment=1
# for i in range(num):
#     inciment=inciment*2
#     print(inciment)

result=list(map((lambda num: 2**num),range(num)))

print(result)