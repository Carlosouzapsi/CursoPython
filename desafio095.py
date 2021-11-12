time = list()
jogador = dict()
partidas = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input('Quantos gols na partida {}? '.format(c + 1))))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! RESPONDA APENAS S ou N.')
    if resp == 'N':
        break
print('-= ' * 30)
print('cod ', end='')
for i in jogador.keys():
    print('{:>15}'.format(i), end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print('{:>3} '.format(k), end='')
    for d in v.values():
        print('{:<15} '.format(str(d)), end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com código da {}! '.format(busca))
    else:
        print('LEVANTAMENTO DO JOGADOR {}: '.format(time[busca]["nome"]))
        for i, g in enumerate(time[busca]['gols']):
            print('No jogo {} fez {} gols'.format(i + 1, g))
print('PROGRAMA ENCERRADO!')

