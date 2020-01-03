count_major = float(input(''))
number_subject = input('').split()
max_value = 0
new_average = 0

for i in range(len(number_subject)):
    value = int(number_subject[i])
    number_subject[i] = value
    if value > max_value:
        max_value = value

for i in range(len(number_subject)):
    value = number_subject[i] / max_value * 100
    new_average += value
   
new_average /= count_major
new_average = round(new_average, 2)
print(new_average)