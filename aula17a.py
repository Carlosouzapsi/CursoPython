#### LISTAS PARTE 1!!
### É POSSÍVEL MUDAR O VALOR DE UMA LISTA EM TEMPO DE EXECUÇÃO!! DIFERENTE DE TUPLAS!!
num = [2,5,9,1]
num[2] = 3
print(num)

### ADICIONANDO UM ELEMENTO AO FINAL DE UMA LISTA!!!!
num.append(7)
print(num)

### ORDENANDO OS VALORES EM UMA LISTA!!!!
num.sort()
print(num)

### ORDENANDO PELA ORDEM INVERSA!!!!
num.sort(reverse=True)
print(num)
#### CONTANDO OS ELEMENTOS DE UMA LISTA!!!!!
print('Essa lista tem {} elementos!!!'.format(len(num)))

#### INSERIR UM VALOR EM UMA DETERMINADA POSIÇÃO!!! EX: INSERINDO O 2 NA POS 0!
num.insert(2, 0)
print(num)

### REMOVENDO ELEMENTOS DE UMA LISTA!!! REMOVENDO O ULTIMO ELEMENTO!!
num.pop()
print(num)
### REMOVENDO ELEMENTOS DE UMA LISTA!!! ELEMENTO UM ELEMENTO PELO INDICE DELE!!!
num.pop(2)
print(num)

### REMOVENDO ELEMENTOS DE UMA LISTA!!! REMOVENDO A PRIMEIRA OCORRENCIA DE UM ELEMENTO NA LISTA
num.insert(2, 2)
num.remove(2)

### MONTANDO CONDICIONAIS PARA TRATAR POSSIVEIS ERROS DE NUMEROS NÃO ESTAREM NAS LISTAS:
# if 4 in num:
#     num.remove(4)
# else:
#     print('Não achei o número 4!!')

### DECLARANDO UMA FORMA MAIS BONITA DE LISTA:
# lista = []
# lista.append(5)
# lista.append(9)
# lista.append(4)

# for v in lista:
#     print('{}...'.format(v), end='')

# lista = list()
# lista.append(5)
# lista.append(9)
# lista.append(4)
# for c, v in enumerate(lista):
#     print('Na posição {} encontrei o valor {}'.format(c, v))
# print('Cheguei ao final da lista.')
#### INSTANCIANDO UMA LISTA E POPULANDO COM VALORES!!!
# lista = list()
# for cont in range(0, 5):
#     lista.append(int(input('Digite um valor: ')))
# print(lista)

### CRIA LIGAÇÕES DE LISTAS, NÃO CÓPIAS!
# a = [2,3,4,7]
# b = a
# b[2] = 8
# print('Lista {}'.format(a))
# print('Lista {}'.format(b))

### FORMA CORRETA DE CRIAR CÓPIAS DE LISTAS NO PYTHON:
a = [2,3,4,7]
b = a[:]
b[2] = 8
print('Lista A{}'.format(a))
print('Lista B{}'.format(b))






