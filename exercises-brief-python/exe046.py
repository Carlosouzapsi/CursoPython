posicao = str(input('Informe a posição no tabuleiro de xadrez: '))
letra = posicao[0].upper()
numero = int(posicao[1])

def verifica_tabuleiro(l, n, p):
    if l in 'A' or l in 'C' or l in 'E' or l in 'F':
        print(f'A posicao {l} começa com quadrado preto.')
    else:
        print(f'A posição {l} começa com quadrado branco.')
    if n % 2 == 0:
        if l in 'A' or l in 'C' or l in 'E' or l in 'F':
            print(f'A posição informada tem quadrado branco.')
    else:
        print(f'A posição informada possui quadrado preto.')



verifica_tabuleiro(letra, numero, posicao)

