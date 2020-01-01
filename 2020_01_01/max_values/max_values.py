values = []
for i in range(9):
    values.append(int(input('')))
max_value = 0
location = 0

for i in range(9):
    if values[i] > max_value:
        max_value = values[i]
        location = i+1
print(max_value)
print(location)