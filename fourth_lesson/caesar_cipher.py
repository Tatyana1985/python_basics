print('Введите от 1 до 25')
n = int(input())
print('Введите строку')
str = input()
text = ''
for i in str:
    if i.isalpha():
        if ord(i) - n < 97:
            s = chr(ord(i) - n + 26)
        else:
            s = chr(ord(i) - n)
        text = text + s
    else:
        text = text + i
print(text)
