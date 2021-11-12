def ficha(jog='<desconhecido>', gol=0):
    print('O jogador {} fez {} no campeonato.'.format(jog, gol))

### PROGRAMA PRINCIPAL:
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)