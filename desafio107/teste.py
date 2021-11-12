from desafio107 import moeda

p = float(input('Digite o preço: R$'))
print('A metade de {} é {}'.format(p, moeda.metade(p)))
print('O dobro de {} é {}'.format(p, moeda.dobro(p)))
print('Diminuindo 13%, temos: {:.2f}'.format(moeda.diminuir(p, 13)))
print('Aumentando 10%, temos: {:.2f}'.format(moeda.aumentar(p, 10)))