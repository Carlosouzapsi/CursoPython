salario = float(input('Qual é o salário do Funcionário? R$'))
novoSalario = salario + ((salario * 15) / 100)
print(f'Um funcionário que ganhava R${salario:.2f} , passou a ganhar: {novoSalario:.2f}')