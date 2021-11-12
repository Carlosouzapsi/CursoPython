import math

l1 = int(input('Informe o primeiro lado do triângulo: '))
l2 = int(input('Informe o segundo lado do triângulo: '))
l3 = int(input('Informe o terceiro lado do triângulo: '))

s = (l1 + l2 + l3) / 2


def calc_area(soma_lados, lado1, lado2, lado3):
    area = math.sqrt(soma_lados * (soma_lados - lado1) * (soma_lados - lado2) * (soma_lados - lado3))
    return area


print(f'Area do triângulo: {calc_area(s, l1, l2, l3)}')