def reloop(upper):
    if upper>0:
        reloop(upper-1)
        print(upper)

upper=int(input("Enter upper limit: "))
reloop(upper)
