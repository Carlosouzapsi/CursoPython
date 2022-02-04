from datetime import date
atual = date.today().year
pessoa = dict()
for p in range(0, 3):
    pessoa['nome'] = str(input('Nome: '))
    pessoa['anoNasc'] = int(input('Ano de Nascimento: '))
    pessoa['ctps'] = int(input('Carteira de Trabalho: '))
    idade = atual - pessoa['anoNasc']
    if pessoa['ctps'] != 0:
        pessoa['anoCont'] = int(input('Digite o ano de contratação: '))
        pessoa['salario'] = float(input('Digite o salário da pessoa: '))
        pessoa['idadeApos'] = idade + 35
for k, v, in pessoa.items():
    print('{} tem o valor {}'.format(k, v))
