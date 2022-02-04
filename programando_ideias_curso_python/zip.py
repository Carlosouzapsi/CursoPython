"""

ZIP -> Retorna um objeto zip com elementos dos iteráveis passados como parâmetros.

-> Pode receber qualquer tipo de iterável.

-> O tamanho do menor iterável predomina.

"""

### Exemplo 1 de zip
# alunos = ['Bianca', 'Vitor', 'Ariel']
# notas = (10, 6, 8)

# juntarTudo = zip(alunos, notas)
# print(juntarTudo)
# print(type(juntarTudo))

# ### OBS: OS VALORES SE PERDEM DEPOIS DE CONVERTER E PRINTAR O ZIP, LOGO PRECISA
# ### OS VALORES SE "PERDEM" DEPOIS DO PRIMEIRO print():


# # print(list(juntarTudo)) ### Transforma os indices iguais em uma tupla
# print(dict(juntarTudo)) ### Transforma os indices em chave e valor

### Exemplos 2 de zip:
# nome = ['Bianca', 'Vitor', 'Ariel', 'José']
# idade = (18, 82, 71, 9, 12)
# cidade = {'São Paulo', 'Vitória', 'São Luís'} ### Conjunto n tem ordenação

# estado = {1: 'RS', 2: 'RJ', 3: 'ES', 4:'AM'}

# print(list(zip(nome, idade, cidade, estado.values())))

### Exemplo 3 de zip:
lugares = [('SP', 'São Paulo'), ('PR', 'Vitória'), ('AM', 'São Luis')]

### Passando o asterisco, ocorrem desempacotamento da lista:
print(list(zip(*lugares)))