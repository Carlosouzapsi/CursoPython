def armazena_dados():
    hab_dicionario = dict()
    hab_lista = list()
    for i in range(1, 5):
        hab_dicionario['nome'] = str(input(f'Informe o nome do habitante {i}: '))
        hab_dicionario['sexo'] = str(input(f'Informe o sexo do habitante {i} (M ou F): ')).upper().strip()[0]
        hab_dicionario['idade'] = int(input(f'Informe a idade do habitante {i}: '))
        hab_dicionario['esporte'] = str(input(f'Informe o esporte favorito do habitante {i}: '))
        ### PRECISA SER ASSIM PARA COPIAR DE FORMA CERTA O DICT PARA DENTRO DA LISTA:
        hab_lista.append(hab_dicionario.copy())
    return hab_lista


lista = armazena_dados()
### IMPRIMINDO A LISTA PARA TESTE:
print(lista)


def calc_media_nat():
    soma_homens = 0
    homens_nat = 0
    soma_idades_homens = 0
    media = 0
    i = 1
    for i in range(0, len(lista)):
        if 'M' in lista[i]['sexo']:
            soma_homens += 1
            soma_idades_homens += lista[i]['idade']
            if lista[i]['esporte'] == 'natação':
                homens_nat += 1
    if homens_nat != 0:
        print(f'Existem {homens_nat} homem(s) cadastrados que gostam de natação')
        media = soma_idades_homens / soma_homens
        print(f'A media de idade de homens que gostam de natação é {media}')
    else:
        msg()


def msg():
    print('Não há homens cadastrados que gostam de natação')


calc_media_nat()
