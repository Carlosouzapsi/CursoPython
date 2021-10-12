print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
p = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão da PA: '))
d = p + (10 -1) * r
for c in range(p, d + r, r):
    print(c, end=' -> ')
print('ACABOU')