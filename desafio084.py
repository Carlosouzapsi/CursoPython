dados = list()
pessoas = list()
maiorPeso = 0
menorPeso = 0
while True:
    dados.append(str(input('Digite o Nome: ')))
    dados.append(float(input('Digite o Peso: ')))
    if len(pessoas) == 0:
        maiorPeso = dados[1]
        menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja continuar cadastrando pessoas? [S/N]: '))
    if opcao in 'Nn':
        break
print('Foram cadastrados um total de {} pessoas.'.format(len(pessoas)))
print('O maior peso foi de {} Kg'.format(maiorPeso))
print('O menor peso foi de {} Kg'.format(menorPeso))
for p in pessoas:
    if p[1] == maiorPeso:
        print('Mais pesados: {}'.format(p[0]))
    if p[1] == menorPeso:
        print('Mais leves: {}'.format(p[0]))


