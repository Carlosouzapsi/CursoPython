temp_c = float(input('Informe a temperatura em Celsius: '))


def conver_fahrenheit(c):
    f = c * 1.8 + 32
    return f

def conver_kelvin(c):
    k = 273 + c
    return k

print(f'Temperatura convertida para Fahrenheit: {conver_fahrenheit(temp_c)} F')
print(f'Temperatura convertida para escala Kelvin: {conver_kelvin(temp_c)} K')



