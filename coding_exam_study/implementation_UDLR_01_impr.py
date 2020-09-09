import time

n = int(input('n= '))
directions = input('direction= ').split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

start_time = time.time()
for direction in directions:
    for i in range(len(move_types)):
        if direction == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            else:
                x, y = nx, ny

end_time = time.time()

print(f'{x}, {y}')
print(f'{end_time - start_time}') #5.245208740234375e-05