print('Введите минимальную, максимальную и текущую длительность сна')
a, b, h = int(input()), int(input()), int(input())
if a > h  and a <= b:
    print('Недосып')
elif a <= h <= b:
    print('Это нормально')
elif  b < h and a <= b:
    print('Пересып')
else:
    print('Введены некорректные данные')