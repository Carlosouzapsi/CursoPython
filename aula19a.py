### FORMAS DE DECLARAR UM DICIONÁRIO:
dados = dict()
### OU
dados = {}

### DECLARANDO UM DICIONARIO:
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

### ACESSANDO CHAVES, VALORES, POR LAÇOS:
for k, v, in pessoas.items():
    print(f'{k} = {v}')

for k in pessoas.values():
    print(f'{k}')

for k in pessoas.keys():
    print(f'{k}')

#### IMPRIMINDO CONTEÚDOS DE UM DICIONÁRIO DE DADOS:
print('O {} tem {} anos '.format(pessoas["nome"], pessoas["idade"]))

### IMPRIMINDO AS KEYS DE UM DICIONÁRIO:
print(pessoas.keys())

### IMPRIMINDO OS VALUES
print(pessoas.values())

### IMPRIMINDO OS ITENS
print(pessoas.items())

### APAGANDO UM ELEMENTO:
del pessoas['sexo']

### DICIONÁRIO DENTRO DE UMA LISTA:
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
#### IMPRIMINDO DICIONARIO DENTRO DE UMA LISTA!!
print(brasil)
### IMPRIMINDO O PRIMEIRO ELEMENTO DA LISTA QUE É O DICIONARIO DE RIO DE JANEIRO:
print(brasil[0])

### IMPRIMINDO A UF DO PRIMEIRO ESTADO DO DICIONÁRIO:
print(brasil[0]['uf'])

#### OUTROS
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    #### Fatiamento de dados para os dados serem salvos corretamente:
    brasil.append(estado.copy())
#### PRINTANDO DE FORMA ELEGANTE:
for e in brasil:
    # for k, v in e.items():
    #     print('O campo {} tem valor {}'.format(k, v))
    for v in e.values():
        print(v, end='')
    print()