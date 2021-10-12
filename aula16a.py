#### TUPLAS SÃO IMUTÁVEIS EM PYTHON!
#### NÃO É POSSÍVEL MUDAR OS ELEMENTOS DE UMA TUPLA EM TEMPO DE EXECUÇÃO!!!
### SOMENTE É POSSÍVEL MUDAR UM ELEMENTO DE UMA TUPLA QUANDO O PROGRAMA ESTÁ PARADO!!!!!
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(lanche)
# print(lanche[0])
# print(lanche[1])
### Fatiando do primeiro ao terceiro elemento:
# print(lanche[1:3])
### Iterando uma tupla
# for comida in lanche:
#     print('Eu vou comer {} '.format(comida))
# print('Comi pra caramba!!!!')
# for cont in range(0, len(lanche)):
#     print('Eu vou comer {} '.format(lanche[cont]))

# for comida in lanche:
#     print('Eu vou comer {}'.format(comida))

# for pos, comida in enumerate(lanche):
#     print('Eu vou comer {} na posicao {}'.format(comida, pos))


# print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
### Colocando uma tupla de forma ordenada:
print(sorted(c))
#### QUANTAS VEZES APARECE UM ELEMENTO NUMA TUPLA:
print(c.count(5))
### PEGANDO A POSICAO DE UMA TUPLA PELO INDEX:
print(c.index(8))
### TUPLAS PODEM TER VÁRIOS TIPOS DE DADOS:
pessoa = ('Carlos', 30, 'M', 99.98)
### TUPLAS PODEM SER DELETADAS INTEIRAS, MAS NÃO DÁ PRA DELETAR ELEMENTOS DELA EM TEMPO DE EXEC!