soma = 0
cont = 0
num = 0

while True:
    num = int(input('Informe um número: '))
    if num == 0 and soma == 0:
        print('O primeiro número não pode ser zero!')
    soma += num
    if num == 0 and soma != 0:
        break
    ### Necessário colocar o contador aqui, para que o zero não seja incrementado.
    cont += 1

print(cont)
media = soma / cont
print(f'Foram digitados {cont}')
print(f'A soma dos números é {soma}')
print(f'A média dos números é: {media}')
