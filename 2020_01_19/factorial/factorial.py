def fact(i):
    return i * fact(i-1) if i > 1 else 1

num = int(input(''))
mulofnum = fact(num)
print(mulofnum)