produtos = list()
for p in range(0, 2):
    preco = float(input(f'Informe o preço do produto {p + 1}: '))
    produtos.append(preco)
print("=" * 35)
print("      TABELA DE PREÇOS       ")
print("=" * 35)
for produto in produtos:
    print(f"U$: {produto:.2f} ----- Desc 60 %: U${produto * 0.6:.2f}")
