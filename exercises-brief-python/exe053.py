pontuacao = float(input('Informe a pontuação: '))

def verifica_pontuacao(p):
    if p == 4:
        print('Conceito A+ ou Conceito A')
    elif p == 3.7:
        print('Conceito A-')
    elif p == 3.3:
        print('Conceito B+')
    elif p == 3.0:
        print('Conceito B')
    elif p == 2.7:
        print('Conceito B-')
    elif p == 2.3:
        print('Conceito C+')
    elif p == 2.0:
        print('Conceito C-')
    elif p == 1.7:
        print('Conceito D+')
    elif p == 1.0:
        print('Conceito F')

verifica_pontuacao(pontuacao)



