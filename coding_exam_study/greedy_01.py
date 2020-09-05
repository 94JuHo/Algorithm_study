#내가 생각한 코드
#거슬러줘야 할 동전의 최소갯수를 구하시오.
#동전별 갯수를 구하는게 아닌, 최소 몇 개의 동전을 사용해야하는가? 에 대한 문제임
import time

exchange_money = [500, 100, 50, 10]
customer_pay = int(input("Pay: "))
price = int(input("Price: "))
exchange_customer = customer_pay - price
num_exchange_money = [0, 0, 0, 0]

start_time = time.time()
for i in range(len(exchange_money)):
    num_exchange = exchange_customer // exchange_money[i]
    extra = exchange_customer % exchange_money[i]
    num_exchange_money[i] = num_exchange
    exchange_customer -= exchange_money[i] * num_exchange

    if exchange_customer == 0:
        break
end_time = time.time()

print(f'Exchange Num-> 500:{num_exchange_money[0]}, 100:{num_exchange_money[1]}, 50:{num_exchange_money[2]}, 10:{num_exchange_money[3]}')
print(f'Time:{end_time-start_time}')
