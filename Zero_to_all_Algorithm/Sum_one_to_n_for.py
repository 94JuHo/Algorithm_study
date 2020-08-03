# Sum of 1 to n via for

print('Sum of 1 to n ')
n = int(input('n: '))

sum = 0
i = 1

for i in range(1, n+1):
    sum += i

print(f'Sum of 1 to {n} is {sum}')
