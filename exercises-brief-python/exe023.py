import math

while True:
    try:
        lado_pol = int(input('Informe a medida do lado do polígono: '))
        num_lados = int(input('Informe o número de lados do poligono: '))
    except ValueError:
        print('Um erro, ocorreu.')
        print('O valor informado deve ser um número inteiro!')
        print('Tente novamente!')
    else:
        break

def calc_area(l, n):
    area = (n * math.pow(l, 2)) / 4 * math.tan(math.pi / n)
    return area


print(f'Area do Poligono: {calc_area(lado_pol, num_lados):.2f}')
