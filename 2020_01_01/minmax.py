words = []
length = int(input(''))
words_tr = input('').split()
for i in range(length):
    words.append(int(words_tr[i]))
words.sort()
print(words[0], words[length-1])