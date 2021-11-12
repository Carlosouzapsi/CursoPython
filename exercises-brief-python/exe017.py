massa = float(input('Informe o valor da massa de H2O em (g): '))
temperatura = float(input('Informe a temperatura em graus celsius: '))
calor_esp_agua = 4.186
q = massa * calor_esp_agua * temperatura
print(f'O valor de energia necessário para aquecer {massa} gramas de H2) é igual {q:.2f} Joules')

def conversorKwh(j):
    conv = j / 360000
    custo = conv * 8.9
    print(f'VALOR CONVERTIDO PARA KW/H: {conv:.2f}')
    return custo

print(f'O custo para ferver {massa} gramas de água é: {conversorKwh(q):.2f} U$')

