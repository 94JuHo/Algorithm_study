number_rest = []
for i in range(10):
    number = int(input('')) % 42
    count = 0
    for j in range(len(number_rest)):
        if number_rest[j] == number:
            count += 1
    if count == 0:
        number_rest.append(number)
print(len(number_rest))