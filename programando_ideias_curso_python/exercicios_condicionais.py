num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
print('Digite + para somar.')
print('Digite - para subtrair')
print('Digite * para multiplicar')
print('Digite / para dividir')

operacao = str(input('Informe o a operação: '))
soma = 0
subtracao = 0
multiplicacao = 0
divisao = 0

if operacao == '+':
    soma = num1 + num2
    print(soma)
elif operacao == '-':
    subtracao = num1 - num2
    print(subtracao)
elif operacao == '*':
    multiplicacao = num1 * num2
    print(multiplicacao)
elif operacao == '/':
    divisao = num1 / num2
    print(divisao)
