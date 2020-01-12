char = input('').split()
num = int(char[0])

try:
    char = char[1]
except:
    char = ""
    
new_char = ""
if char.isalnum():
    for i in char:
        for j in range(num):
            new_char += i
    print(new_char)