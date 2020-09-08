import time

row, col = map(int, input('row, col= ').split())
big = 0

start_time = time.time()
for i in range(0, row):
    data = list(map(int, input('data= ').split()))
    data.sort()
    if big < data[0]:
        big = data[0]

end_time = time.time()
print(big)
print(f'{end_time - start_time}') #4.83
