matriz = [[0,0,0], [0,0,0],[0,0,0]]
somaPares = 0
maiorValor = 0
somaColunas = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor: [{}. {}]: '.format(l, c)))
# print(matriz)
print('=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print('[{}]'.format(matriz[l][c]), end=' ')
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
    print()
print('=' * 30)
print('A soma dos valores pares é {}'.format(somaPares))
for l in range(0, 3):
    somaColunas += matriz[l][2]
print('A soma dos valores da terceira coluna é {}'.format(somaColunas))
for c in range(0, 3):
    if c == 0:
        maiorValor = matriz[1][c]
    elif matriz[1][c] > maiorValor:
        maiorValor = matriz[1][c]
print('O maior valor da segunda linha é: {}'.format(maiorValor))