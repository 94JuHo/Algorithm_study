def fibo(i):
    return  i if i <=1 else fibo(i-1) + fibo(i-2) 

i = int(input(''))
num = fibo(i)
print(num)