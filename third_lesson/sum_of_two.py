print('Введите натуральное число n >= 2')
n = int(input())
print('Введите целое число')
a = int(input())
sumList = list()
for i in range(n - 1):
    print('Введите целое число')
    b = int(input())
    sumList.append(a + b)
    a = b
print(sumList)