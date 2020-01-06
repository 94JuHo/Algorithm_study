number = int(input(''))
case = []
avg = []

for i in range(number):
    case.append(input('').split())

for i in range(number):
    for j in range(len(case[i])):
        case[i][j] = int(case[i][j])

sum_average_arr = []
for i in range(number):
    sum_average = 0
    for j in range(1, len(case[i])):
        sum_average += case[i][j]
    sum_average /= case[i][0]
    sum_average_arr.append(sum_average)

for i in range(number):
    count = 0
    for j in range(1, len(case[i])):
        if case[i][j] > sum_average_arr[i]:
            count += 1
    avg.append(float(count/case[i][0]) * 100)

for i in range(len(avg)):
    print('{0:.3f}%'.format(avg[i]))