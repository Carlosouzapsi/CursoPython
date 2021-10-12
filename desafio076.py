listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90)
print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end='')
    else:
        print('R$ {:>7.2f}'.format(listagem[pos]))
print('-' * 30)