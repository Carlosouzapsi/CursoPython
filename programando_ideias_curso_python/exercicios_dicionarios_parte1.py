herois = dict()
armas_heroi = dict()
vilao = {'nome': 'thanos', 'nivel': 150}
cont = 0
print(len(herois))
while True:
    try:
        cont += 1
        nome = str(input(f'Informe o nome do herói {cont}: '))
        herois[nome] = int(input(f'Informe o nível do herói {cont}: '))
        arma = str(input(f'Informe o nome da arma do personagem {cont}: '))
        armas_heroi[arma] = int(input(f'Informe o nível da arma do herói {cont}: '))
        print(armas_heroi[arma])
    except ValueError:
        print('É necessário informar um valor válido.')
    else:
        if cont == 1:
            break
while True:
    print('ESCOLHER HERÓI CADASTRADO:')
    for contador_opcoes in range(1, len(herois)):
        print(f'INFORME {contador_opcoes} PARA JOGAR COM O HERÓI {contador_opcoes}')
    print('INFORME 4 PARA SAIR')
    opcao_escolhida = int(input('OPÇÃO ESCOLHIDA: '))
    if opcao_escolhida == 1:
        print('VOCÊ ESCOLHEU JOGAR COM O HERÓI 1! ')
        print('INFORMAÇÕES DO HERÓI 1: ')
        heroi_info = 0
        poder_total = 0
        for k, v, in herois.items():
            heroi_info += 1
            print(f'NOME: {k} NIVEL HEROI: {v}')
            poder_total += herois[nome]
            if heroi_info == 1:
                break
        for k, v, in armas_heroi.items():
            heroi_info += 1
            print(f'NOME ARMA: {k} NIVEL ARMA: {v}')
            poder_total += armas_heroi[arma]
            break
        print(f'PODER TOTAL DO HERÓI: {poder_total}')
        print('BOA SORTE NA SUA LUTA!')
        print(f"NOME DO VILÃO: {vilao['nome']} PODER VILAO: {vilao['nivel']}")
        if vilao['nivel'] > poder_total:
            print('VITÓRIA DO VILÃO')
        else:
            print('VITÓRIA DO HERÓI')

cont_herois = 0
for k, v, in herois.items():
    print(f'NOME HEROI: {k} NIVEL HEROI: {v}')
for k, v, in armas_heroi.items():
    print(f'NOME ARMA: {k}  NIVEL ARMA: {v}')
    ('=' * 30)
