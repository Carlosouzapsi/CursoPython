import math

while True:
    try:
        peso = float(input('informe o peso da pessoa em KG: '))
        altura = float(input('Informe a altura da pessoa em metros: '))
    except ValueError:
        print('Erro, valores informados incorretos, tente novamente!')
    else:
        break

def calc_imc(p, a):
    imc = p / math.pow(a, 2)
    return imc


print(f'Valor do IMC: {calc_imc(peso, altura):.2f}')

