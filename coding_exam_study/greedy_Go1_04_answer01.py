import time

n, k = map(int, input('n, k= ').split())
result = 0

start_time = time.time()
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1
end_time = time.time()
print(result)
print(f'{end_time - start_time}') # 9.5367431640625e-06
