from desafio109 import moeda

p = float(input('Digite o preço: R$'))
print('A metade de {} é {}'.format(moeda.moeda(p), moeda.metade(p, True)))
print('O dobro de {} é {}'.format(moeda.moeda(p), moeda.dobro(p, True)))
print('Diminuindo 13%, temos: {}'.format(moeda.diminuir(p, 13, True)))
print('Aumentando 10%, temos: {}'.format(moeda.aumentar(p, 10, True)))