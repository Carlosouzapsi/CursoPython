salarioAtual = float(input('Digite o salário atual do funcionário: '))
perc10 = (salarioAtual * 10 ) / 100
perc15 = (salarioAtual * 15) / 100

if salarioAtual <= 1250.00:
    novoSalario = salarioAtual + perc10
elif salarioAtual > 1250.00:
    novoSalario = salarioAtual + perc15
print('O salário com aumento é de: R$ {} o antigo salário era: R$ {} '.format(novoSalario, salarioAtual))