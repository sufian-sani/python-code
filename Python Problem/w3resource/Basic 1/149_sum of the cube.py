def sumcube(num):
    num-=1
    sun_add=0
    while(num>0):
        sun_add+=num**3
        num-=1
    return sun_add

num=int(input("Take positive intiger: "))
print(sumcube(num))