import time

n = int(input('n= '))
directions = list(input('direction= ').split())
start = [1, 1]

start_time = time.time()
for direction in directions:
    if direction == 'U':
        if start[0] == 1:
            continue
        else:
            start[0] -= 1

    if direction == 'D':
        if start[0] == n:
            continue
        else:
            start[0] += 1

    if direction == 'L':
        if start[1] == 1:
            continue
        else:
            start[1] -= 1

    if direction == 'R':
        if start[1] == n:
            continue
        else:
            start[1] += 1

end_time = time.time()
print(f'{start[0]}, {start[1]}')
print(f'{end_time - start_time}') #1.0013580322265625e-05