import time

n, m, k = map(int, input('n, m, k= ').split())

data = list(map(int, input('data= ').split()))

data.sort()
Big_first = data[n - 1]
Big_second = data[n - 2]

start_time = time.time()

count = (m // (k+1)) * k
count += m % (k+1)

result = 0
result += count * Big_first
result += (m - count) * Big_second

end_time = time.time()

print(result)
print(f'{(end_time - start_time)}') # 8.821487426757812e-06
