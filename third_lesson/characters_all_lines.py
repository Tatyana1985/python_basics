print('Введите натуральное число')
n = int(input())
characters = list()
for i in range(n):
    print('Введите строку')
    s = input()
    characters.extend(list(s))
print(characters)


