kg_pascal = float(input('Informe a temperatura em Kg Pascal: '))

def conversor(p):
    conv = p * 7.5006157593
    return conv


print(f'O valor convertido para mg de mercúrio é: {conversor(kg_pascal):.2f}')
