def verifica_nota(c, s):
    pontuacao = 0
    if c in 'A':
        if s in '+':
            pontuacao = 4.0
            return pontuacao
        if s in '-':
            pontuacao = 3.7
            return pontuacao
        if s != '-' and s != '+':
            pontuacao = 4.0
            return pontuacao
    if c in 'B':
        if s in '+':
            pontuacao = 3.3
            return pontuacao
        if s in '-':
            pontuacao = 2.7
            return pontuacao
        if s != '-' and s != '+':
            pontuacao = 3.0
            return pontuacao
    if c in 'C':
        if s in '+':
            pontuacao = 2.3
            return pontuacao
        if s in '-':
            pontuacao = 1.7
            return pontuacao
        if s != '-' and s != '+':
            pontuacao = 2.0
            return pontuacao
    if c in 'D':
        if s in '-':
            pontuacao = 1.3
            return pontuacao
        if s != '-' and s != '+':
            pontuacao = 1.0
            return pontuacao
    if c in 'F':
        pontuacao = 0
        return pontuacao


somaPontuacao = 0
contador = 0
flag = False
while not flag:
    letra = str(input('Informe a letra e/ou sinal referente a sua nota: ')).strip()
    if letra == '':
        contador = 1
        flag = True
        print('Programa encerrado pela linha em branco do usuário.')
    else:
        caractere = letra[0].upper()
        if len(letra) < 2:
            sinal = ' '
        else:
            sinal = letra[1]
        nota = verifica_nota(caractere, sinal)
        somaPontuacao += nota
        contador += 1

media = somaPontuacao / contador
print(f'Valor da soma da pontuação: {somaPontuacao}')
print(f'Valor do contador: {contador}')
print(f'Média das notas: {media}')
