entrada = 0
soma_entradas = 0
while True:
    idade = str(input('Informe a idade da pessoa: '))
    if idade != "":
        idade = int(idade)
    else:
        print('Programa encerrado com sucesso!')
        break
    if idade <= 2:
        entrada = 0
    if idade >= 3 and idade <= 12:
        entrada = 14
    if idade > 12 and idade < 65:
        entrada = 23
    if idade >= 65:
        entrada = 18

    soma_entradas += entrada

print(f'Valor total cobrado nas entradas: R$ {soma_entradas:.2f}')
