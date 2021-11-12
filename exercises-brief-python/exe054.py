
invalido = True
desc_desempenho = ' '
while invalido:
        rank = float(input('Informe o rank atingido pelo funcionário: '))
        if rank == 0.0:
            desc_desempenho = 'Ruim'
            invalido = False
        elif rank == 0.4:
            desc_desempenho = 'Médio'
            invalido = False
        elif rank >= 0.6:
            desc_desempenho = 'Bom'
            invalido = False
        else:
            print('Erro, valor digitado inválido.')

aumento = 2400 * rank
print(f'O desempenho do funcionário foi: {desc_desempenho}')
print(f'O aumento recebido foi de {aumento}')
salario_final = aumento + 2400
print(f'O salario final é de {salario_final}')


