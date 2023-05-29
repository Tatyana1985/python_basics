print("Введите числа через запятую")
sequence = map(int, input().split(','))
listSeq = list(sequence)
tupleSeq = tuple(listSeq)
print('Список:', listSeq)
print('Кортеж:', tupleSeq)


