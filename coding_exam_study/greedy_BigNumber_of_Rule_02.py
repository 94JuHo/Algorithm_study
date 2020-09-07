import time

n, m, k = map(int, input('n, m, k= ').split())
data = list(map(int, input('data= ').split()))

data.sort()
Big_first = data[n-1]
Big_second = data[n-2]

result = 0
num = k

start_time = time.time()
for i in range(m, 0, -1):
    if num == 1:
        num = k
        result += Big_second
        continue
    result += Big_first
    num -= 1
end_time = time.time()

print(result)
print(f'{end_time-start_time}')