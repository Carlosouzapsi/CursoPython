from random import randint
from time import sleep
from operator import itemgetter
resultados = dict()
for c in range(1, 5):
    resultados['Jogador {}'.format(c)] = randint(1,6)
for k, v in resultados.items():
    print('O jogador {} tirou {}'.format(k, v))
    sleep(1)
#### CRIANDO UM SEGUNDO DICIONÁRIO PARA ORDENAR O PRIMEIRO:
ranking = dict()
#### USANDO UM REVERSE PRA ORDENAR DE FORMA DESCRESCENTE E USANDO ITEM GETTER PRA ORDENAR:
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('=' * 30)
print('Ranking dos Jogadores: ')
for i, v in enumerate(ranking):
    print('{}o lugar: {} com {}'.format(i + 1, v[0], v[1]))











