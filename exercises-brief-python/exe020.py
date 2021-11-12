litro_gas = float(input('Informe a quantidade de gas em litros: '))

def calc_gas(v):
    tempK = 273.15 + 20
    p = 20000000
    r = 8.314
    t = tempK
    n = v * p / t * r
    return n


print(f'O número de mols de gas no tanque é: {calc_gas(litro_gas):.2f} mols')


