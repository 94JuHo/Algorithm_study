import time

h_time = int(input('time= '))

# hh:mm:ss
count = 0

start_time = time.time()

for h in range(h_time + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

end_time = time.time()

print(count)
print(f'{end_time - start_time}') #0.017162561416625977