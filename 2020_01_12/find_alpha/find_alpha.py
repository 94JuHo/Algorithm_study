alpha = [-1 for i in range(26)]
char = input('')
count = 0
for i in char:
    num = ord(i) - 97
    if 0<=num<=26 and alpha[num] is -1:
        alpha[ord(i)-97] = count
    count += 1
print(''.join(str(e)+' ' for e in alpha))