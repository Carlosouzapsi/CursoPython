import math

while True:
    try:
        num1 = int(input('Informe o valor de a: '))
    except ValueError:
        print('Erro, você precisa digitar valores válidos.')
        print('Informe números um número inteiro para cada uma das variáveis.')
    else:
        break
while True:
    try:
        num2 = int(input('Informe o valor de b: '))
    except ValueError:
        print('Erro, você precisa digitar valores válidos.')
        print('Informe números um número inteiro para cada uma das variáveis.')
    else:
        break
while True:
    try:
        num3 = int(input('Informe o valor de c: '))
    except ValueError:
        print('Erro, você precisa digitar valores válidos.')
        print('Informe números um número inteiro para cada uma das variáveis.')
    else:
        break

def calc_equacao(a, b, c):
    delta = math.pow(a, 2) - (4 * a * c)
    if delta < 0:
        print(f'A equação não possui raízes reais. Valor de delta é: {delta}')
    elif delta == 0:
        r1 = math.sqrt(delta) - b / (2 * a)
        print('O valor de delta é zero.')
        print(f'A equação possui apenas uma raiz real igual a {r1}')
    elif delta > 0:
        r1 = math.sqrt(delta) + b / (2 * a)
        r2 = math.sqrt(delta) - b / (2 * a)
        print(f'As raízes da equação são: {r1:.2f}')
        print(f'As raízes da equação são: {r2:.2f}')

calc_equacao(num1, num2, num3)











