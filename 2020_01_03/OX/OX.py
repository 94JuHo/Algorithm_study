count = int(input(''))
score = []
result = []
for i in range(count):
    score.append(input(''))

for i in range(count):
    jumsu = 0
    jumsu_result = 0
    for j in range(len(score[i])):
        if score[i][j] == 'O':
            if score[i][j-1] == 'O':
                jumsu += 1
                jumsu_result += jumsu
            else:
                jumsu = 1
                jumsu_result += jumsu
        else:
            jumsu = 1
    result.append(jumsu_result)

for i in range(len(result)):
    print(result[i])