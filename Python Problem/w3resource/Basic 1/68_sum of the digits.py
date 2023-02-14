n=int(input())

# print(n%10)
main_add=0
while(n>0):
    sum_add=n%10
    main_add+=sum_add
    n=n//10

print(main_add)