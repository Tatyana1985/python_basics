print('Введите натуральное число')
n = int(input())
divisors = list()
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print(divisors)

