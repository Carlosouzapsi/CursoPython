# Equação de segundo grau: a * x ** 2 + b * x + c
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b ** 2) - (4 * a * c)

## Resumo da parte final de bhaskara:
## Na matemática elevar um número a meio é o mesmo que tirar a raiz dele!
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print(f'As raízes são: {x1} e {x2}')
