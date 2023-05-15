print('Введите строку')
str = input()
s = 0
for i in str:
    if 97 <= ord(i) <= 122:
        s = s + 1
print(s)
