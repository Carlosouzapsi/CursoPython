while True:
    try:
        base = int(input('Informe a base do triângulo: '))
        alt = int(input('Informe a altura do triângulo: '))
    except ValueError:
        print('Algo deu errado, por favor tente novamente.')
        print('Você deve digitar um número inteiro.')
    else:
        break


def calc_area(b, a):
    area = b * a / 2
    return area


print(f'Valor da área do triângulo: {calc_area(base, alt):.2f}')
