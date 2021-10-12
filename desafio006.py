n = int(input('Digite um número:'))
d = n * 2
t = n * 3
### fazendo a metade da potencia para encontrar a resposta da raiz quadrada:
r = n ** (1/2)
print(f'O dobro de {n} vale {d}')
### Quebra de linha e formatação no python:
print(f'O triplo de {n} é {t} . \nA raiz quadrada de {n} é igual a {r:.2f}')

### raiz quadrada com o método pow:
resultadoRaiz = pow(n, (1/2))
print(f'resultado raiz com método é {resultadoRaiz:.2f}')