valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
qtdAnos = int(input('Quantos anos vai demorar a ser pago: '))

prestacaoMensal = valorCasa / (qtdAnos * 12)

print('Valor da casa em R${:.2f}'.format(valorCasa))
print('Total de anos de pagamento: {}'.format(qtdAnos))
print('Valor da prestação R${:.2f}'.format(prestacaoMensal))

limitePercSalario = (salario * 30) / 100

if prestacaoMensal > limitePercSalario:
    print('Empréstimo negado!')
elif prestacaoMensal < limitePercSalario:
    print('Empréstimo liberado!')






