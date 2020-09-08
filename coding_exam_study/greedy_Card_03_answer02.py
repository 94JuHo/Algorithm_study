import time

n, m = map(int, input('n, m=').split())

result = 0

start_time = time.time()
for i in range(n):
    data = list(map(int, input('data= ').split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result= max(result, min_value)
end_time = time.time()
print(result)
print(f'{end_time - start_time}') #5.487