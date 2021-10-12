valores = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    opcao = str(input('Você quer continuar? [S/N]: ')).strip()[0]
    if opcao in 'Nn':
        break
print('Você digitou {} elementos'.format(len(valores)))
valores.sort(reverse=True)
print('Os valores em ordem descrescente são {}:'.format(valores))
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
