import math

altura = float(input('Informe a altura da pessoa: '))
peso = float(input('Informa o peso da pessoa: '))

imc = peso / math.pow(altura, 2)

print('O IMC calculado é: {:.2f}'.format(imc))

if imc < 18.5:
    print('A pessoa está abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('A pessoa está no peso ideal')
elif imc > 25 and imc <= 30:
    print('A pessoa está com sobrepeso')
elif imc > 30 and imc <= 40:
    print('A pessoa é obesa')
elif imc > 40:
    print('Obesidade mórbida')