def return_sum(num):
    if num<=1:
        return num
    else:
        return num + return_sum(num-1)

num=int(input('Take intiger: '))
print(return_sum(num))
