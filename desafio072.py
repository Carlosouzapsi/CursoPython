contagemEscrita = ('zero', 'um', 'dois', 'três')
print(contagemEscrita)

while True:
    numero = int(input('Digite um número entre 0 e 3: '))

    if numero >= 0 and numero <= 3:
    # if 0 <= numero <= 3: forma simplificada!
        break
    print('Tente novamente. ', end='')
print('Você digitou o número {}'.format(contagemEscrita[numero]))

