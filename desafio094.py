pessoas = dict()
dados = list()
mulheres = list()
acima = list()
media = 0
totIdade = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Informe o nome da pessoa: '))
    while True:
        pessoas['sexo'] = str(input('Informe o sexo da pessoa [M/F]:'))
        if pessoas['sexo'] in 'Mm' or pessoas['sexo'] in 'Ff':
            break
        else:
            print('ERRO! TENTE NOVAMENTE!')
    if pessoas['sexo'] in 'Ff':
        mulheres.append(pessoas.copy())
    pessoas['idade'] = int(input('Informe a idade da pessoa: '))
    totIdade+=pessoas['idade']
    if len(dados) != 0:
        media = totIdade / len(dados)
    elif len(dados) == 0:
        media = pessoas['idade']
    if pessoas['idade'] > media:
        acima.append(pessoas.copy())
    dados.append(pessoas.copy())
    opcao = str(input('Você deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
print('O número de pessoas cadastradas foi: {}'.format(len(dados)))
print('A média de idades cadastradas é: {} '.format(media))
print('A lista de mulheres cadastradas é: {}'.format(mulheres))
print('A lista de pessoas acima da média de idade é {}'.format(acima))

