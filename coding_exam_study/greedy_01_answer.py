import time

n = int(input("Exchange money: "))
count = 0

list = [500, 100, 50, 10]
start_time = time.time()
for coin in list:
    count += n // coin
    n %= coin
end_time = time.time()
print(count)
print(f'Time:{end_time-start_time}')