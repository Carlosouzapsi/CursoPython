from random import randint

resultado = ''
cara_coroa = 0
jogadas = int(input('Quantas vezes você deseja jogar a moeda?'))
cont = 0
resultado_cara = 0
resultado_coroa = 0
while jogadas > cont:
    cara_coroa = randint(1, 2)
    if cara_coroa == 1:
        resultado = 'Cara'
        resultado_cara += 1
    else:
        resultado = 'Coroa'
        resultado_coroa += 1
    cont += 1

print(f'Foram feitas {jogadas} jogadas.')
print(f'Resultados: {resultado_cara} Cara')
print(f'Resultados: {resultado_coroa} Coroa')
