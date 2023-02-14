def knapsack(v,w,C):
	N = len(v)
	m = {}
	for c in range(C+1):
		m[(0,c)] = 0
	for i in range(1,N+1):
		for c in range(C+1):
			if w[i-1] <= c:
				m[(i,c)] = max(m[(i-1),c], v[i-1] + m[(i-1,c-w[i-1])])
			else:
				m[(i,c)] = m[(i-1),c]
	return m[(N,C)]

n,w=map(int,input().split())
it_v=[]
it_w=[]
for i in range(n):
	v,w_p=map(int,input().split())
	it_v.append(v)
	it_w.append(w_p)

print(knapsack(it_v,it_w,w))
# # A Dynamic Programming based Python
# # Program for 0-1 Knapsack problem
# # Returns the maximum value that can
# # be put in a knapsack of capacity W
# def knapSack(W, wt, val, n):
# 	K = [[0 for x in range(W + 1)] for x in range(n + 1)]
#
# 	# Build table K[][] in bottom up manner
# 	for i in range(n + 1):
# 		for w in range(W + 1):
# 			if i == 0 or w == 0:
# 				K[i][w] = 0
# 			elif wt[i-1] <= w:
# 				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
# 			else:
# 				K[i][w] = K[i-1][w]
#
# 	return K[n][W]
#
# # Driver program to test above function
# nt,W=map(int,input().split())
# val=[]
# wt=[]
# for _ in range(nt):
#     v,w_p=map(int,input().split())
#     val.append(v)
#     wt.append(w_p)
#
# n = len(val)
# print(knapSack(W, wt, val, n))

# This code is contributed by Bhavya Jain


# def max_value(it_v,it_w):
#     max_v=0
#     indexed=0
#     for i in range(len(it_v)):
#         if it_v[i]/it_w[i] >=max_v:
#             max_v=it_v[i]/it_w[i]
#             indexed = i
#     return max_v,indexed
#
# it_v=[60,100,120]
# it_w=[20,50,30]
# print(max_value(it_v,it_w))

# # print(50-20)
#
# # A naive recursive implementation
# # of 0-1 Knapsack Problem
#
# # Returns the maximum value that
# # can be put in a knapsack of
# # capacity W
#
#
# def knapSack(W, wt, val, n):
#
# 	# Base Case
# 	if n == 0 or W == 0:
# 		return 0
#
# 	# If weight of the nth item is
# 	# more than Knapsack of capacity W,
# 	# then this item cannot be included
# 	# in the optimal solution
# 	if (wt[n-1] > W):
# 		return knapSack(W, wt, val, n-1)
#
# 	# return the maximum of two cases:
# 	# (1) nth item included
# 	# (2) not included
# 	else:
# 		return max(
# 			val[n-1] + knapSack(
# 				W-wt[n-1], wt, val, n-1),
# 			knapSack(W, wt, val, n-1))
#
# # end of function knapSack
#
#
# #Driver Code
# n,W=map(int,input().split())
# val=[]
# wt=[]
# for _ in range(n):
# 	v,w_p=map(int,input().split())
# 	val.append(v)
# 	wt.append(w_p)
#
# n_len = len(val)
# print(knapSack(W, wt, val, n_len))
#
# # This code is contributed by Nikhil Kumar Singh

# def fractional_knapsack(value, weight, capacity):
# 	"""Return maximum value of items and their fractional amounts.
#
#     (max_value, fractions) is returned where max_value is the maximum value of
#     items with total weight not more than capacity.
#     fractions is a list where fractions[i] is the fraction that should be taken
#     of item i, where 0 <= i < total number of items.
#
#     value[i] is the value of item i and weight[i] is the weight of item i
#     for 0 <= i < n where n is the number of items.
#
#     capacity is the maximum weight.
#     """
# 	# index = [0, 1, 2, ..., n - 1] for n items
# 	index = list(range(len(value)))
# 	# contains ratios of values to weight
# 	ratio = [v / w for v, w in zip(value, weight)]
# 	# index is sorted according to value-to-weight ratio in decreasing order
# 	index.sort(key=lambda i: ratio[i], reverse=True)
#
# 	max_value = 0
# 	fractions = [0] * len(value)
# 	for i in index:
# 		if weight[i] <= capacity:
# 			fractions[i] = 1
# 			max_value += value[i]
# 			capacity -= weight[i]
# 		else:
# 			fractions[i] = capacity / weight[i]
# 			max_value += value[i] * capacity / weight[i]
# 			break
#
# 	return max_value, fractions
#
# n,capacity=map(int,input().split())
# value=[]
# weight=[]
# for _ in range(n):
# 	v,w_p=map(int,input().split())
# 	value.append(v)
# 	weight.append(w_p)
#
#
# max_value, fractions = fractional_knapsack(value, weight, capacity)
# print('The maximum value of items that can be carried:', max_value)
# print('The fractions in which the items should be taken:', fractions)
