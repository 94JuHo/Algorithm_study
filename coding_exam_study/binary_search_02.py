n = int(input('Input num:'))
array = [0] * 1000000

for i in input('Number:').split():
    array[int(i)] = 1

m = int(input('Customer num:'))
x = list(map(int, input('Customer number:').split()))

for i in x:
    if array[i] == 1:
        print('yes ', end='')
    else:
        print('no ', end='')

print()

