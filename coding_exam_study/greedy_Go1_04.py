import time

n, k = map(int, input('n, k= ').split())
i = 0

start_time = time.time()
while n != 1:
    i += 1

    if n % k == 0:
        n = n // k
    else:
        n -= 1
end_time = time.time()

print(i)
print(f'{end_time - start_time}') #8.344650268554688e-06