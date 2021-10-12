import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
### resolução tradicional sem bibliotecas do python:
hi = (co ** 2 + ca ** 2) ** (1/2)

print(f'A hipotenusa vai medir {hi:.2f}')

### Utilizando módulos:
h1 = math.hypot(co, ca)
print(f'A hipotensua vai medir {h1:.2f}')


