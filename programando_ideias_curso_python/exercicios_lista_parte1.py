produtos = list()
precos = list()
contador = 0
continuar = False
soma_precos = 0
while True:
    item_carr = str(input(f'Informe o nome do produto {contador + 1}: '))
    produtos.append(item_carr)
    item_prec = float(input(f'Informe o preço do produto {contador + 1} :'))
    precos.append(item_prec)
    soma_precos += item_prec
    contador += 1
    while not continuar:
        opcao = str(input('Deseja adicionar mais algum produto[S/N] ? ')).upper()[0]
        if 'S' in opcao:
            break
        elif 'N' in opcao:
            print('Programa encerrado pelo usuário.')
            continuar = True
            break
        else:
            print('Opção inválida, tente novamente.')
    ### Condição de saída geral do loop:
    if continuar:
        break
print("Listas: ")
print(f'Items do carrinho: {produtos}')
print(f'Preço dos items do carrinho {precos}')
print(f'Valor total dos itens {soma_precos:.2f} R$')
