# sum of n to n via for

print('sum of n to n')
number1 = int(input('num 1: '))
number2 = int(input('num 2: '))

if number1 > number2:
    number1, number2 = number2, number1

sum = 0
for i in range(number1, number2+1):
    sum += i

print(f'Sum of {number1} to {number2} is {sum}')