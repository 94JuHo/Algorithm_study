import time

n = int(input('n= '))
x, y = 1, 1
plans = input('direction= ').split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

start_time = time.time()
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue

            x, y = nx, ny

end_time = time.time()

print(f'{x}, {y}')
print(f'{end_time - start_time}') #5.2928924560546875e-05