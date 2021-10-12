valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor Duplicado. Não vou adicionar.')
    opcao = str(input('Você quer continuar? [S/N]: ')).strip()[0]
    if opcao in 'Nn':
        break

valores.sort()
print(valores)