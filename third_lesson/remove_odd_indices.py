print('Введите натуральное число n')
n = int(input())
indices = list()
for i in range(n):
    print('Введите целое число')
    indices.append(int(input()))
del indices[1::2]
print(indices)

# for i in range(len(indices)):
#     if i%2 !=0:
#         del indices[i]
# print(indices)
