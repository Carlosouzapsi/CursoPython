print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
p = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão da PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total+=mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo+=r
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')