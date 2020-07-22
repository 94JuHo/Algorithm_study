# input 3 number and Max number calculate

print('Calculate 3 number')
a = int(input('Input num A: '))
b = int(input('Input num B: '))
c = int(input('Input num C: '))

maximum = a
if b > maximum:
    maximum = b

if c > maximum:
    maximum = c

print(f'Max number is {maximum}')
