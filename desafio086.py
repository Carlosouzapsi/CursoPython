matriz = [[0,0,0], [0,0,0],[0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor: [{}. {}]: '.format(l, c)))
# print(matriz)
print('=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print('[{}]'.format(matriz[l][c]), end=' ')
    print()