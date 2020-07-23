# input 3 number and Max number calculate using def

def max_of_number(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c

    return maximum

print(f'max_of_number(3, 2, 1) = {max_of_number(3, 2, 1)}')
print(f'max_of_number(3, 2, 2) = {max_of_number(3, 2, 2)}')
print(f'max_of_number(3, 1, 2) = {max_of_number(3, 1, 2)}')
print(f'max_of_number(3, 2, 3) = {max_of_number(3, 2, 3)}')
print(f'max_of_number(2, 1, 3) = {max_of_number(2, 1, 3)}')
print(f'max_of_number(3, 3, 2) = {max_of_number(3, 3, 2)}')