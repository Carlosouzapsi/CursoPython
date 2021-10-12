valores = list()
### OU
# valores = []

maior = 0
menor = 0
for v in range(0, 5):
    valores.append(int(input('Digite o valor {} da lista: '.format(v))))
    if v == 0:
        maior = valores[v]
        menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print('=' * 30)
print('O maior valor digitado foi: {} nas posições: '.format(maior), end='')
print('O menor valor digitado foi: {} nas posições: '.format(menor))
for i, v in enumerate(valores):
    if v == maior:
        print('o Indice do maior valor é {}'.format(i))
for i, v in enumerate(valores):
    if v == menor:
        print('O Indice do menor valor é {}'.format(i))

