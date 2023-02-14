import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# def value_finder(it_v,it_w,max_value):
#     # print(it_v)
#     # print(max_value)
#     indexed = 0
#     for i in range(len(it_v)):
#         if it_v[i] / it_w[i] >= max_value:
#             max_value = it_v[i] / it_w[i]
#             indexed = i
#     return max_value,indexed
#
#
# n,w=map(int,input().split())
# it_v=[]
# it_w=[]
# for i in range(n):
#     v,w_p=map(int,input().split())
#     it_v.append(v)
#     it_w.append(w_p)
#
# # print(it_v)
# # print(it_w)
# # print(value_finder(it_v,it_w))
# max_value = 0
# indexed = 0
# max_loot = []
# while w>0:
#     # print(max_value)
#     max_value_intia, indexed = value_finder(it_v,it_w,max_value)
#     max_value=max_value_intia
#     if it_w[indexed] <= w:
#         max_loot.append(it_v[indexed])
#         w = w - it_w[indexed]
#         # print(it_v[indexed])
#         it_v.pop(indexed)
#         it_w.pop(indexed)
#     else:
#         max_weight=it_v[indexed]/it_w[indexed]
#         weight_gain=max_weight*w
#         max_loot.append(weight_gain)
#         # print(it_v[indexed])
#         # print(it_w[indexed])
#         break

# print(round(sum(max_loot),5))
# print("{:.5f}".format(sum(max_loot)))
# print(max_loot)


# print(max_value)
# print(indexed)
'''
def knapsack(n, capacity, value_list, weight_list):
    unitValues_list = []

    #First lets calculate the unitValues_list
    for i in range(n):
        unitValue = (value_list[i]/weight_list[i])
        unitValues_list.append(unitValue)

    #Now lets fill the knapsack, intake is how much is in the bag at the moment!
    intake = 0
    max_value = 0
    factor = True

    while(factor):
        max_index = unitValues_list.index(max(unitValues_list, default=0))
        # this gives the index of the max valued element

        if(weight_list[max_index] <= capacity):
            # In this case, full item is taken in
            intake = weight_list[max_index]
            capacity -= weight_list[max_index]
            max_value += value_list[max_index]

        else:
            # weight_list[max_index] > capacity
            # In this case, fraction to be taken
            fraction = capacity / weight_list[max_index]
            max_value += value_list[max_index]*fraction
            capacity = int(capacity - (weight_list[max_index] * fraction))

        weight_list.pop(max_index)
        value_list.pop(max_index)
        unitValues_list.pop(max_index)
        # print(weight_list)

        n -= 1 #no. of items left
        factor = ((n != 0) if ((capacity != 0) if True else False) else False)

    return max_value

if __name__ == "__main__":
    value_list = []
    weight_list = []

    #The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
    #The next 𝑛 lines define the values and weights of the items.

    # n , capacity = map(int, input('n, capacity: ').split())
    n , capacity = map(int, input().split())

    for i in range (n):
        # value , weight = map(int, input('value, weight: ').split())
        value , weight = map(int, input().split())
        value_list.append(value)
        weight_list.append(weight)

    #Output the maximal value of fractions of items that fit into the knapsack.
    print("{:.5f}".format(knapsack(n, capacity, value_list, weight_list)))
'''
# n,w=map(int,input().split())
# ls=[]
# for _ in range(n):
#     it_v,it_w=map(int,input().split())
#     ls.append((it_v,it_w))
#
# max_v=0
# max_v_w=0
# for max_val in range(n):
#     if max_v < ls[max_val][0]:
#         max_v = ls[max_val][0]
#         max_v_w = ls[max_val][1]
#
# v_capasity=0
#
# while w>0:
#     if w>max_v_w:
#         v_capasity=max_v
#         w=w%max_v_w
#
#
#
# print(v_capasity)
#
#
#
# # print(ls[max_val][0])

