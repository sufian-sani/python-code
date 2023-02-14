def dec_bin(num):
    if num > 1:
        dec_bin(num//2)
    print(num%2,end=' ')


num=int(input('Take intiger: '))
dec_bin(num)