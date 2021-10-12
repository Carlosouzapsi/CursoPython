print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
p = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão da PA: '))
termo = p
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end=' ')
    # print(' x ' if cont < 1 else ' ', end = ' ')
    termo+=r
    cont+=1
print('FIM!')

