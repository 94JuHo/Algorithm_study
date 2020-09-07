import time

n, m, k = map(int, input('n, m, k= ').split())

data = list(map(int, input('data= ').split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

start_time = time.time()

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second

end_time = time.time()

print(result)
print(f'{(end_time - start_time)}') # 1.1682510375976562e-05