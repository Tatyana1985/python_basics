print('Введите длины сторон треугольника')
a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
else:
    print('Треугольник с заданными длинами сторон не существует, должно выполняться неравенство треугольника:',
          'a + b > c, a + c > b, b + c > a', sep='\n')



