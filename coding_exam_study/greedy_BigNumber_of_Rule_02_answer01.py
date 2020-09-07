import time

n, m, k = map(int, input('n, m, k= ').split())

data = list(map(int, input('data= ').split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
start_time = time.time()
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
end_time = time.time()
print(result)
print(f'{end_time - start_time}')
