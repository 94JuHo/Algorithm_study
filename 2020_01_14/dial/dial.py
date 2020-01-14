def find(word):
    dial = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],
['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
    for i in range(len(dial)):
        for j in range(len(dial[i])):
            if dial[i][j] == word:
                return i+2

word = input('')
word_sum = 0
for i in word:
    word_sum += find(i)
word_sum += len(word)
print(word_sum)