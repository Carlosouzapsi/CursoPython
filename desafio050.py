
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}o número: '.format(c)))
    if n % 2 == 0:
        soma+=n
        cont+=1
print('A soma dos pares é: {}'.format(soma))
print('A total de pares digitados foi: {}'.format(cont))