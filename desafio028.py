## importando somente a parte de randomizar inteiros do modulo:s
from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "pensar"
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
jogador = int(input('Em que número eu pensei? '))
print('Processando...') # Brincadeira pra fazer o computador passa ideia de que está realmente pensando!!
sleep(3)
if jogador == computador:
    print('Parábens! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}'.format(computador, jogador))

