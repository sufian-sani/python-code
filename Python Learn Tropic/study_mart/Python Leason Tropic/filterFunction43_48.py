number = [1,2,3,4,-5,6,7,-8,9]

# result = list(filter((lambda n:n%2==0),number))
result = list(filter((lambda n:n<0),number))
print(result)