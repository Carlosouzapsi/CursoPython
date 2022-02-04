# result = randint(0, 38)
result = 2
print(result)

if result % 2 != 0 or result == 30 or result == 32 or result == 34 or result == 36:
    print(f'Número do sorteio: {result}')
    print("Paga Vermelho.")
elif result % 2 == 0 and result != 37 and result != 38:
    print(f'Número do sorteio: {result}')
    print("Paga Preto.")
if result == 37:
    print(f"Número do sorteio: 00")
    print("Paga Verde, dinheiro para casa.")
if result == 38:
    print(f"Número do sorteio: 0")
    print("Paga Verde, dinheiro para casa.")
