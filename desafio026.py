### colocando uma string digitada desde o inicio em caixa alta:
frase = str(input('Digite uma frase: ')).upper().strip()

### Verificando a quantidade de letras 'A':
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
### Verificando a primeira posição da letra 'A':
print('A primeira letra A apareceu pela primeira vez na posição {}'.format(frase.find('A') + 1))
### Verificando a partir do lado direito a letra 'A':
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))