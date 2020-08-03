# input 3 number and calculate middle number

def Middle_3Num_Calc(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

def Middle_3Num_Calc_ver2(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

print('Calculate middle number')
a = int(input('Num a: '))
b = int(input('Num b: '))
c = int(input('Num c: '))

print(f'Middle Num is {Middle_3Num_Calc(a, b, c)}.')