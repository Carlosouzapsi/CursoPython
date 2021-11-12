### Calcular a área de uma sala:

def areaSala(altura, largura):
    area = altura * largura
    print(f'A área da sala é de {area:.2f}m2')

a = float(input('Digite o valor da altura da sala: '))
l = float(input('Digite o valor da largura da sala: '))
print(areaSala(a, l))
