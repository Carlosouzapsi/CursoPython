letra = str(input('Informe a letra e o sinal referente a sua nota: ')).strip()
caractere = letra[0].upper()
if len(letra) < 2:
    sinal = ' '
else:
    sinal = letra[1]

print(len(letra))
print(letra)

def verifica_nota(c, s):
    if c in 'A':
        if s in '+':
            print(f'Pontuação: 4.0')
        if s in '-':
            print(f'Pontuação: 3.7')
        if s != '-' and s != '+':
            print(f'Pontuação: 4.0')
    if c in 'B':
        if s in '+':
            print(f'Pontuação: 3.3')
        if s in '-':
            print(f'Pontuação: 2.7')
        if s != '-' and s != '+':
            print(f'Pontuação: 3.0')
    if c in 'C':
        if s in '+':
            print(f'Pontuação: 2.3')
        if s in '-':
            print(f'Pontuação: 1.7')
        if s != '-' and s != '+':
            print(f'Pontuação: 2.0')
    if c in 'D':
        if s in '-':
            print(f'Pontuação: 1.3')
        if s != '-' and s != '+':
            print(f'Pontuação: 1.0')
    if c in 'F':
        print(f'Pontuação: 0')




verifica_nota(caractere, sinal)





