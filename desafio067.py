
n = 0
c = 1
while True:
    n = int(input('Digite o número que você deseja ver a tabuada: '))
    while c <= 10:
        print(' {} x {} = {}'.format(n, c, n * c))
        c += 1
    c = 0
    if n < 0:
        break
print('O número que foi digitado é negativo, programa encerrado.')
