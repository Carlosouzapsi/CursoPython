import math
import emoji
### Importando módulos de funções matemáticas no python
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print(f'A raiz de {num} é: {raiz:.2f}')

### Emote de óculos:
print(emoji.emojize('Olá mundo:sunglasses:', use_aliases=True))

### outra forma de importar:
### from math import sqrt
### Sintaxe fica:
### raiz = sqrt(num)