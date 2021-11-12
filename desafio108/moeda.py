def aumentar(preco = 0, aut = 0):
    res = preco + ((preco * aut)/100)
    return res

def diminuir(preco = 0, sub = 0):
    res = preco - ((preco * sub)/100)
    return res

def dobro(preco= 0):
    dobroPreco = preco * 2
    return dobroPreco


def metade(preco= 0):
    metadePreco = preco / 2
    return metadePreco

def moeda(preco = 0, moeda = 'R$'):
    return '{}{:.2f}'.format(moeda, preco).replace('.', ',')


