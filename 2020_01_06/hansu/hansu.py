def han(x):
    hansu_count=0
    for i in range(1, x+1):
        if i<100:
          hansu_count+=1
        else:
            hansu = []
            for j in str(i):
                hansu.append(int(j))
            if hansu[0]-hansu[1] == hansu[1]-hansu[2]:
                hansu_count += 1
    return hansu_count
num = [110, 1, 210, 1000]
for i in num:
    print(han(i))