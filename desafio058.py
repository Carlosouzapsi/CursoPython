from random import randint

computador = randint(1,10) # Faz o computador "pensar"
jogador = 0
numeroDePalpites = 0
while jogador != computador:
    numeroDePalpites+=1
    jogador = int(input('EM QUAL NÚMERO ESTOU PENSANDO??? Tente advinhar: '))
    print('HAHAHAHA!, VOCÊ ERROU! TENTE NOVAMENTE!')
print('O QUE? EU PERDI??? NÃÃÃÃOOOOO, EU VOLTAREI!!!!')
print('O número de tentativas foi: {}'.format(numeroDePalpites))



