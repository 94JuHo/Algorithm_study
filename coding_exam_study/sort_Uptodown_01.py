n = int(input('n= '))

array = []
for i in range(n):
    array.append(int(input('data= ')))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
