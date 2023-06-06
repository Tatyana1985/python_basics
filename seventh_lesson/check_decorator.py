def hash(func):
    def wrapper():
        print('###')
        func()
        print('###')
    return wrapper

@hash
def print_bill():
    print('Данные чека')


print_bill()