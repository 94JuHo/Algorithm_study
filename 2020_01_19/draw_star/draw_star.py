def draw_star(k):
    for i in range(k):
        for j in range(k):
            if i % 3 == 1 and j % 3 == 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()


num = int(input(''))
draw_star(num)