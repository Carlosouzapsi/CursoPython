ano = int(input('Informe o ano que você deseja analisar: '))

def verifica_ano(a):
    if a % 400 == 0:
        print('Ano é bissexto')
    elif a % 100 == 0:
        print('Não é um ano bissexto')
    elif a % 4 == 0:
        print('Não é um ano bissexto')
    else:
        print('Não é um ano bissexto')

verifica_ano(ano)