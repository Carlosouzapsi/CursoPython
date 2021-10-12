valores = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    opcao = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if opcao in 'Nn':
        break

print('Lista geral: {} '.format(valores))
print('Lista pares: {} '.format(pares))
print('Lista ímpares: {} '.format(impares))


