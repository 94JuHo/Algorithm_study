music_tr = input('').split()
music = []
for i in range(8):
    check = int(music_tr[i])
    music.append(check)
asc = 1
desc = 1
for i in range(1,8):
    if music[i-1]+1 == music[i]:
        asc += 1
    elif music[i-1]-1 == music[i]: 
        desc += 1
if asc == 8:
    print('ascending')
elif desc == 8:
    print('descending')
else:
    print('mixed')