move = input('Insert Your Location: ')

# a1
row = int(move[1]) #1
column = int(ord(move[0]) - int(ord('a'))) + 1 # 알파벳 기준으로 순서구하기

steps = [ # 이동 가능한 모든 경우의 수
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
