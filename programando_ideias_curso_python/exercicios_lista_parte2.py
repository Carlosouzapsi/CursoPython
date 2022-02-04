jogos = list()
jogos_venda = list()
preco_fabrica = list()
vendas = list()


def resumo_loja():
    if len(vendas):
        print(f'VALOR TOTAL VENDIDO: R$ {sum(vendas)}')
        print('JOGOS AINDA EM ESTOQUE: ')
        for j in jogos:
            print(f'NOME: {j}', end=" ")
        for p in preco_fabrica:
            print(f'PRECO: {p}')
    else:
        print(f'NÃO FORAM CADASTRADAS VENDAS ATÉ O MOMENTO!')


def registrar_venda():
    if len(jogos):
        print('LISTA DE JOGOS CADASTRADOS:')
        cont = 0
        for j in jogos:
            cont += 1
            print(cont, 'NOME:', j, end='')
        for p in preco_fabrica:
            print(f' PREÇO: R$ {p:.2f}')
        try:
            cod_venda = int(input('INFORME O CÓDIGO DO JOGO QUE VOCÊ DESEJA VENDER: '))
            indice_lista = cod_venda - 1
            vendas.append(preco_fabrica[indice_lista])
            jogos.pop(indice_lista)
            preco_fabrica.pop(indice_lista)
            print('JOGO VENDIDO COM SUCESSO!')
        except:
            ('NÃO EXISTEM JOGOS CADASTRADOS COM ESSE CÓDIGO!')
        else:
            ('VENDA EFETUADA COM SUCESSO!')
    else:
        print('AINDA NÃO FOI REGISTRADO NENHUM JOGO. COMPRE NO ESTOQUE PARA PODER CONSULTAR!')


def compra_estoque():
    while True:
        nome_jogo = input("NOME DO JOGO: ")
        preco_jogo = input("PRECO DE FÁBRICA: ")
        print("PARA SAIR DIGITE UM ESPAÇO EM BRANCO.")
        if nome_jogo != "":
            jogos.append(nome_jogo)
            preco_jogo = float(preco_jogo)
            preco_fabrica.append(preco_jogo)
        else:
            print('Saindo do estoque!')
            break


def imprime_menu():
    print("=" * 30)
    print('        LOJA DE JOGOS       ')
    print("=" * 30)
    print("DIGITE UMA DAS OPÇÕES ABAIXO: ")
    print("=" * 30)
    print("1 - REGISTRAR VENDA")
    print("2 - COMPRAR ESTOQUE")
    print("3 - RESUMO LOJA")
    print("4 - SAIR")
    print("=" * 30)


## PROGRAMA PRINCIPAL:
opcao_escolhida = 0
while opcao_escolhida != 4:
    imprime_menu()
    opcao_escolhida = input("OPÇÃO ESCOLHIDA: ")
    if opcao_escolhida != "":
        opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            registrar_venda()
        if opcao_escolhida == 2:
            compra_estoque()
        if opcao_escolhida == 3:
            print('AINDA NÃO IMPLEMENTADO!')
            resumo_loja()
    else:
        print("PROGRAMA DA LOJA ENCERRADO. VOLTE SEMPRE!")
        break
