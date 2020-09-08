import time

n, k = map(int, input('n, k= ').split())
result = 0

start_time = time.time()
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
end_time = time.time()
print(result)
print(f'{end_time - start_time}') #1.4066696166992188e-05