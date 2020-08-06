# sum of n to n verbose 1

print('sum of n to n')
number1 = int(input('input number1: '))
number2 = int(input('input number2: '))

if number1 > number2:
    number1, number2 = number2, number1

sum = 0
for i in range(number1, number2 + 1):
    if i < number2:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum += i

print(sum)