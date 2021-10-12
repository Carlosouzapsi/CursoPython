totgasto = 0
mais1000 = 0
NomeMenor = ''
precoMenor = 0
cont = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    totgasto+=preco
    if preco >= 1000:
        mais1000+=1
    if cont == 1:
        precoMenor = preco
        nomeMenor = produto
    else:
        if preco < precoMenor:
            precoMenor = preco
            nomeMenor = produto
    if continuar == 'N':
        break
print('Programa encerrado!')
print('O total gasto foi: R$ {}'.format(totgasto))
print('Existem {} produtos que custam mais que R$ 1000,00'.format(mais1000))
print('O produto mais barato custa R$ {} '.format(preco))
print('O nome do produto mais barato é {}'.format(nomeMenor))



