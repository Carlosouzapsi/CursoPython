def aumentar(preco = 0, aut = 0, formato=False):
    res = preco + ((preco * aut)/100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, sub = 0, formato=False):
    res = preco - ((preco * sub)/100)
    return res if formato is False else moeda(res)

def dobro(preco= 0, formato=False):
    dobroPreco = preco * 2
    return dobroPreco if formato is False else moeda(dobroPreco)


def metade(preco= 0, formato=False):
    metadePreco = preco / 2
    return metadePreco if formato is False else moeda(metadePreco)

def moeda(preco = 0, moeda = 'R$'):
    return '{}{:.2f}'.format(moeda, preco).replace('.', ',')

def resumo(preco=0, taxaa=10,taxar=5):
    print('-' * 30)
    print('RESUMO VALOR'.center(30))
    print('-' * 30)
    print('Preço analisado: {}'.format(moeda(preco)))
    print('Dobro do preço: {}'.format(dobro(preco, True)))
    print('Metade do preço: {}'.format(metade(preco, True)))
    print(f'{taxaa}% de aumento: {aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: {diminuir(preco, taxar, True)}')
    print('-' * 30)


