def solve(a):
    sum_arr = 0
    for i in range(len(a)):
        sum_arr += a[i]
    return sum_arr

a = [1, 2, 3, 4, 5, 6]
print(solve(a))
