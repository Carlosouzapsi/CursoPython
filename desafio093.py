jogador = dict()
qtdGols = list()
partidas = 0
totgols = 0
for j in range(0, 1):
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
    for g in range(0, partidas):
        gols = int(input('Quantos gols na partida? {} : '.format(g)))
        totgols+=gols
        qtdGols.append(gols)
    jogador['gols'] = qtdGols
    jogador['total'] = totgols
print('=' * 30)
print(jogador)
print('=' * 30)
for k, v, in jogador.items():
    print('{} tem o valor {}'.format(k, v))
for p, g in enumerate(qtdGols):
    print('Na partida {}, fez {} gols'.format(p, g))
print('Foi um total de {} gols'.format(totgols))





