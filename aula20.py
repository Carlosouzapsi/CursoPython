### FUNÇÕES EM PYTHON
# def lin():
#     print('-' * 30)
#
# lin()
# print(' CURSO EM VIDEO ')
# lin()
# print(' APRENDA PYTHON ')
# lin()
# print(' GUSTAVA GUANABARA ')
# lin()

### TRABALHANDO COM PARÂMETROS
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

#### O VALOR DE MENSAGEM FOI PASSADO POR PARÂMETRO!!!
mensagem('CURSO EM VIDEO')
mensagem('APRENDA PYTHON')
mensagem('GUSTAVO GUANABARA')

def soma(a, b):
    s = a + b
    print('Resultado da soma é: {}'.format(s))


### PROGRAMA PRINCIPAL:
# soma(1, 2)
# ### OU
# soma(a=4, b=5)

### USANDO RECURSO DE EMPACOTAMENTO DO PYTHON:
### CRIAÇÃO DE UMA TUPLA EM TEMPO DE EXECUÇÃO
# def contador(*num):
#     for valor in num:
#         print(valor, end=' ')
# def contador(*num):
#     tam = len(num)
#     print('Recebi os valores {} e são ao todo {} números.'.format(num, tam))
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

#### USANDO FUNÇÕES PARA TRABALHAR COM LISTAS:
valores = [6, 3, 9, 1, 0, 2]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


dobra(valores)
print(valores)


