#
# #### VERIFICANDO TIPOS PRIMITIVOS EM PYTHON:
# print(type(2)) ### -> Tipo inteiro.
# print(type(2 + 0j)) ### -> Tipo complexo.
# print(type(True)) ### -> Tipo Booleano
# print(type('123')) ### -> Tipo String
# print(type(1.2345)) ### -> Tipo Float
# print(type(False)) ### -> Booleano
# print(type("'2j'")) ### -> String
# print(type(10 + 1j)) ### -> Complexo
# print(type(2)) ### -> Inteiro
# print(type('Programando ideias')) ### -> Tipo String

###2)
nome = str(input('Nome: '))
nota = float(input('Nota: '))
### .title transforma as primeiras letras em maiusculas.
print(f'{nome.title()} tirou {nota}')