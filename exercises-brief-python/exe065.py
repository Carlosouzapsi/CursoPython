print("=" * 30)
print("TABELA DE TEMPERATURAS")
print("=" * 30)
for c in range(0, 110, 10):
    f = (c * 1.8) + 32
    print(f"Celsius: {c} --- Fahreinheit: {f}")
