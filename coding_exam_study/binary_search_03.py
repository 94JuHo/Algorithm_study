n = int(input('Input num:'))
array = set(map(int, input('Number:').split()))

m = int(input('Customer num:'))
x = list(map(int, input('Customer number:').split()))

for i in x:
    if i in array:
        print('yes ', end='')
    else:
        print('no ', end='')
print()

