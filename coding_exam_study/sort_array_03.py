n, k = map(int, input('n, k= ').split())
a = list(map(int, input('a= ').split()))
b = list(map(int, input('b= ').split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
