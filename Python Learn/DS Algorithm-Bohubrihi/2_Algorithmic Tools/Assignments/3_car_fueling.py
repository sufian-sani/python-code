def mainrefills(x,n,l):
    currentRefill = 0
    numRefill = 0
    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n and x[currentRefill+1] - x[lastRefill] <= l):
            currentRefill = currentRefill+1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= n:
            numRefill = numRefill + 1
    return numRefill+1

distance = int(input())
miles = int(input())
n = int(input())
oil_station = list(map(int,input().strip().split()))[:n-1]
oil_station.append(distance)
number_of_station = len(oil_station)-2
# print(oil_station)
# print(number_of_station)

number_refeill = mainrefills(oil_station,number_of_station,miles)
print(number_refeill)