def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    num+=1
    while not is_prime(num):
        num+=1
    return num

print('Введите натуральное число')
num = int(input())

print(get_next_prime(num))



