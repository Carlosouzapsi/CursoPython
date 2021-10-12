num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=' * 30)
print('Os valores pares digitados foram: {}'.format(num[0]))
print('Os valores impares digitados foram: {}'.format(num[1]))