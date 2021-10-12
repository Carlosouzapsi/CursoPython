import math

num = float(input('Digite um valor:'))
inteira = math.trunc(num)
print(f'O valor digitado foi {num} e sua porção inteira é {inteira}')

### Usando a função interna int:
print(f'O valor digitado foi {num} e sua parte inteira é {int(num)}')