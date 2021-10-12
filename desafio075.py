# num1 = int(input('Digite o primeiro valor'))
# num2 = int(input('Digite o segundo valor'))
# num3 = int(input('Digite o terceiro valor'))
# num4 = int(input('Digite o quarto valor'))
#
# numeros = (num1, num2, num3, num4)

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
### Os números ficarão armazenados em uma tupla!!!!!!
print('Você digitou os valores {}'.format(num))
print('O valor 9 apareceu {} vezes'.format(num.count(9)))
if 3 in num:
    print('O valor 3 apareceu na posição {}a posicao'.format(num.index(3)+1))
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


# for pos, comida in enumerate(lanche):
#     print('Eu vou comer {} na posicao {}'.format(comida, pos))

# for pos, numeros in enumerate(numeros):
#     if 3 in numeros:




