cont = 0
m = int(input('Informe o primeiro número: '))
n = int(input('Informe o segundo número: '))
d = min(n, m)
while n % d != 0 or m % d != 0:
    d = d - 1

print(f'O maior divisor comuim entre {n} e {m} é {d}')
