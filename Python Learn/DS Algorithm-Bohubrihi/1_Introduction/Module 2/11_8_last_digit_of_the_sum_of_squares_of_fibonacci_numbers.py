def pisano_num_mod10(n):
   previous, current = 0, 1
   n=n%60 #num mod 10 gives 60 repeatations in Pisano Series.. Check Wikipedia by searching for Pisano Series to get more Info
   if (n == 0):
       return 0
   elif (n == 1):
       return 1
   else:
       for _ in range(2,n+1):
           previous, current= current, (previous + current)%60
       return current
if __name__ == '__main__':
    n = int(input())
    print(pisano_num_mod10(n)*pisano_num_mod10(n+1)%10)

# # Uses python3
# from sys import stdin
#
# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#     sum      = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current
#
#     return sum % 10
#
# if __name__ == '__main__':
#     n = int(stdin.read())
#     print(fibonacci_sum_squares_naive(n))

# # Python3 Program to find sum of
# # squares of Fibonacci numbers
#
# # Function to calculate sum of
# # squares of Fibonacci numbers
# def calculateSquareSum(n):
#     fibo = [0] * (n + 1)
#     if (n <= 0):
#         return 0
#     fibo[0] = 0
#     fibo[1] = 1
#
#     # Initialize result
#     sum = ((fibo[0] * fibo[0]) + (fibo[1] * fibo[1]))
#
#     # Add remaining terms
#     for i in range(2, n + 1):
#         fibo[i] = (fibo[i - 1] + fibo[i - 2])
#         sum += (fibo[i] * fibo[i])
#
#     return sum
#
#
# # Driver Code
# n = int(input())
#
# print("Sum of squares of Fibonacci numbers is :",calculateSquareSum(n))
#
# # This Code is contributed by mits
