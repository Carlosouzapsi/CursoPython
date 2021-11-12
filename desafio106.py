c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m'  # 5 - roxo
     '\033[7;30m'     # 6 - branco
     )

def ajuda(com):
    titulo('Acessando o manual do comando \'{}\''.format(com), 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')

### PROGRAMA PRINCIPAL:
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
