from random import randint

numero1 = randint(0, 5)
numero2 = randint(0, 5)
numero3 = randint(0, 5)
numero4 = randint(0, 5)
numero5 = randint(0, 5)

numeros = (numero1, numero2, numero3, numero4, numero5)
print('Os números gerados foram: {}'.format(numeros))
# RESOLUÇÃO ABAIXO É A TRADICIONAL!!!!!
# maior = 0
# menor = 0
# for cont in range(0, len(numeros)):
#     if cont == 1:
#         maior = numeros[cont]
#         menor = numeros[cont]
#     else:
#         if numeros[cont] > maior:
#             maior = numeros[cont]
#         if numeros[cont] < menor:
#             menor = numeros[cont]
# print('O maior número é {}'.format(maior))
# print('O menor número é {}'.format(menor))
#### RESOLUÇÃO ELEGANTE DO PYTHON!!!!
print('O maior número é {}'.format(max(numeros)))
print('O menor número é {}'.format(min(numeros)))



