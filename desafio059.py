
print('''''')

flag = False
somar = 0;
multiplicacao = 0;
maior = 0;
while flag != True:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    print('''Qual operação você deseja fazer:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Digite a opção do Menu: '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma dos valores é: {}'.format(soma))
    elif opcao == 2:
        multiplicacao = num1 * num2
        print('A multiplicação dos valores é: {}'.format(multiplicacao))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
            print('O maior valor é: {}'.format(maior))
        if num2 > num1:
            maior = num2
            print('O maior valor é: {}'.format(maior))
    elif opcao == 4:
        print('informe novos valores: ')
    elif opcao == 5:
        flag = True
print('Programa encerrado!')