import time

n, m = map(int, input('n, m= ').split())

result = 0

start_time = time.time()
for i in range(n):
    data = list(map(int, input('data= ').split()))
    min_value = min(data)
    result = max(result, min_value)

end_time = time.time()
print(result)
print(f'{end_time-start_time}') #5.348