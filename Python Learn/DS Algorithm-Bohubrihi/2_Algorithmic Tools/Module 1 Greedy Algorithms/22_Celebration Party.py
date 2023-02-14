# Assume that array x is sorted from smallest to largest values
# x_0 <= x_1 <= x_2 <= ... <= x_n-1


def points_covered_sorted(x, n):
    result = []
    i = 0
    while i < n:
        l, r = x[i], x[i]+1
        result.append((l, r))
        i = i + 1
        while i < n and x[i] <= r:
            i = i + 1
    return result


# n = 6
# x = [0.5, 0.9, 1.5, 2.4, 4.5, 5.2]
x = [3.2, 3.8, 4.6, 5]
n = len(x)
print(points_covered_sorted(x, n))