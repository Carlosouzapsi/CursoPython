#### OBTENDO AJUDA INTERATIVA DO PRÓPRIO PYTHON:
# help(print)
### DENTRE OUTROS COMANDOS...

#### DOCSTRINGS => STRINGS DE DOCUMENTAÇÃO
# def contador(i, f, p):
#     """
#     comentários em bloco pra explicar as coisas...
#     :param i:
#     :param f:
#     :param p:
#     :return:
#     """
#     c = i
#     while c <= f:
#         print(c, end=' ')
#         c+=p
#     print('FIM!')
#
# contador(0, 100, 10)


### FUNÇÕES COM PARÂMETROS OPCIONAIS:
# def somar(a, b, c=0):
#     s = a + b + c
#     print('A soma vale {}'.format(s))

# somar(3,2,5)
#### CHAMANDO A FUNÇÃO COM UM PARAMETRO A MENOS PQ TEM UM OPCIONAL:
# somar(3,2)


#### ESCOPO DE VARIÁVEIS:
### Já manjo!!!! xD
### FORÇANDO O ESCOPO DE UMA VARIÁVEL COM PYTHON:
# def teste(b):
#     ### COMANDO GLOBAL FORÇA A VARIAVEL A TER O MESMO VALOR DA GLOBAL
#     global a
#     # a = 8
#     b+=4
#     c = 2
#     print('Valor de a {}'.format(a))
#     print('Valor de b {}'.format(b))
#     print('Valor de c {}'.format(c))
#
# a = 5
# teste(a)
# print('Valor de a {}'.format(a))

### COMANDO RETURN
# def somar(a, b, c):
#     s = a + b + c
#     return s
#
# r1 = somar(3, 2, 5)
# print('O resultado foi {}'.format(r1))

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f
n = int(input('Digite um número: '))
print(fatorial(n))
### RETURN PODE SER USADO PRA RETORNAR OUTROS TIPOS DE VALORES TAMBÉM!!!
