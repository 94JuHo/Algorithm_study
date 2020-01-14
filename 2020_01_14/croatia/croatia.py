word = input('')
word_count = 0
start = 0

croatia_word = [['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']]
for i in range(len(croatia_word[0])):
    for j in range(len(croatia_word[0])):
        croatia = str(croatia_word[0][j])
    
        if word.find(croatia, start) != -1:
            word_count += 1
            start += len(croatia)

word_count += len(word) - start
print(word_count)