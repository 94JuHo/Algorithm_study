number1 = int(input(''))
number2 = int(input(''))
number3 = int(input(''))

result = number1 * number2 * number3
number_str = str(result)
num_str = []
count_zero = 0

for i in range(1, 10):
    count = 0
    for j in range(len(number_str)):
        if int(number_str[j]) == i:
            count += 1
        if i==9 and int(number_str[j]) == 0:
            count_zero += 1
    num_str.append(count)
print(count_zero)
for i in range(9):
    print(num_str[i])