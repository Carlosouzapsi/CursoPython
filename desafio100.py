from random import randint
from time import sleep

numeros = list()

def sorteia(lista):
    print('Sorteando 5 números da lista!!')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print('{}'.format(n), end=' ', flush=True)
        sleep(0.3)
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma+=valor
    print('Somando os valores pares de {} temos {}'.format(lista, soma))

sorteia(numeros)
print(numeros)
somaPar(numeros)


