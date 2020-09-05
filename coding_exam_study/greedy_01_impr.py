import time

exchange_list = [500, 100, 50, 10]
exchange_to_customer = int(input('Exchange money: '))

coin_count = 0
start_time = time.time()
for coin in exchange_list:
    coin_count += exchange_to_customer // coin
    exchange_to_customer %= coin
end_time = time.time()
print(f'Minimum exchange coin number: {coin_count}')
print(f'Time: {end_time-start_time}')