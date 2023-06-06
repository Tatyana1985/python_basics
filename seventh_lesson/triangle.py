import math


class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        #self.triangle()

    def triangle(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return print('Это треугольник')
        else:
           return print('Это не треугольник')

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        return Triangle(a, b, c)

class RightTriangle(Triangle):
    def __init__(self, a, b, c = 0):
        self.a = a
        self.b = b
        self.c = math.sqrt(a*a + b*b)
        #self.triangle()

    def area(self):
        return self.a*self.b/2




print("Введите длины катетов треугольника")
a, b = int(input()), int(input())
print("Введите длины сторон треугольника")
a1, b1, c1 = int(input()), int(input()), int(input())

rtr = RightTriangle(a, b)
tr = Triangle(a1, b1, c1)

print(rtr.c)
print(rtr.area())
print(rtr.perimeter())
addTr = rtr + tr
print(addTr.c)
