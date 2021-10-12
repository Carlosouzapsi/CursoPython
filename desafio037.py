num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} em BINÁRIO, é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} em OCTAL, é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} em HEX, é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')