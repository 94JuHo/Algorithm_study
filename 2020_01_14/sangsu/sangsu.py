num1, num2 = input('').split()
num1, num2 = int(num1), int(num2)
n_num1, n_num2 = 0, 0

n_num1 = (num1 // 100) + ((num1 // 10) % 10) * 10 + (num1 % 10) * 100
n_num2 = (num2 // 100) + ((num2 // 10) % 10) * 10 + (num2 % 10) * 100

print(max(n_num1, n_num2))