# car_milees = 10
# oil_capacity = 100
#
# # end_point = 1800
# end_point = 2200
# # fa_oil_sta = 400
# # sec_oil_sta = 900
# # thi_oil_sta = 1500
# # oil_sta = [400,900,1500]
# oil_sta = [400,900,1500]
#
# re_fule = []
# counter = 0
#
# total_car_milees = car_milees*oil_capacity
#
# for i in range(len(oil_sta)):
#     if total_car_milees>oil_sta[i] and total_car_milees<oil_sta[i+1]:
#         counter = counter+1
#     re_fule.append(counter)
#
# print(re_fule)
#
#
#
# def min_refills(x,n,L):
#     numRefill = 0
#     currentRefill = 0
#     while currentRefill <= n:
#         lastRefill = currentRefill
#         while(currentRefill<=n and x[currentRefill+1]-x[lastRefill]<=L):
#             currentRefill = currentRefill+1
#             if currentRefill == lastRefill:
#                 return 'IMPOSSIBLE'
#             if currentRefill <= n:
#                 numRefill = numRefill +1
#         return numRefill
#
# n = 12
# l = 250
# x = [0,200,375,550,750,850,1000,1200,1500,1600,2000,2200,2600]
# print(min_refills(x,n,l))

# 950
#
# 400
#
# 4
#
# 200 375 550 750

# car_milees = 5
# oil_capacity = 600
# oil_sta = [400,900,1500,1800,2200,2500]
# print(min_refills(oil_sta,car_milees,oil_capacity))

# def car_fueling(dist,miles,n,gas_stations):
#     num_refill, curr_refill, limit = 0,0,miles
#     while limit < dist:  # While the destination cannot be reached with current fuel
#         if curr_refill >= n or gas_stations[curr_refill] > limit:
#             # Cannot reach the destination nor the next gas station
#             return -1
#         # Find the furthest gas station we can reach
#         while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
#             curr_refill += 1
#         num_refill += 1  # Stop to tank
#         limit = gas_stations[curr_refill] + miles  # Fill up the tank
#         curr_refill += 1
#     return num_refill
#
# # Test cases
# print(car_fueling(950, 400, 4, [200, 375, 550, 750]))  # 2
# print(car_fueling(10, 3, 4, [1, 2, 5, 9]))  # -1


# def refuling_counter(o_s,o_c,c_m):
#     fuel_counter = 0
#     current_refuling_loop = 0
#     number_o_s = len(o_s)
#     can_long_distance = o_c*c_m
#     while current_refuling_loop <= number_o_s:
#         if (o_s[current_refuling_loop+1] + o_s[current_refuling_loop]) >= can_long_distance:
#             current_refuling_loop = current_refuling_loop+1
#             print(current_refuling_loop)
#
#     return current_refuling_loop
#
#
#
#
# car_milees = 10
# oil_capacity = 50
# oil_sta = [200,400,800,1000,1200,1500,1600]
#
# print(refuling_counter(oil_sta,oil_capacity,car_milees))


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

# x = [29421,37204,41977,44712,46780,56656,56682,56884,56990,57064,57066,57067,57069,57072,57073,57074,57075,57076,57077,57078,57079,57080,57081,57082,57083,57084,57085,57086,57087,57088,57089,57090]
# x = [105,193,234,351,415,511,530,578,619,649,713,784,849,863,980,1075,1119,1149,1224,1297,1406]
# n = len(x)-2
# l = 121
#
# number_refeill = mainrefills(x,n,l)
# print(number_refeill)

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

# oil_station=[]
# for i in range(n):
#     x = list(map(int, input().split()))
    # N = int(input())
    # oil_station = list(map(int, input().split()))
    # value=int(input().split())
    # oil_station.append(value)
# num = [int(x) for x in input().split()]

# print(distance)
# print(miles)
# print(n)
# print(oil_station)












