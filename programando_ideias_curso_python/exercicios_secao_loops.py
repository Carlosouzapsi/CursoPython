anterior = 0
proximo = 1
parada = 1
soma_termos = 0
while parada <= 5:
    # print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    divisor = 1
    num_divisores_inteiros = 0
    while divisor <= proximo:
        if proximo % divisor == 0:
            num_divisores_inteiros += 1
        divisor += 1
    if num_divisores_inteiros == 2:
        soma_termos += proximo
        # print(proximo)
        parada += 1

media = soma_termos / 5
print(f'Resultado da média dos 5 primeiros termos de fibonnaci: {media}')
