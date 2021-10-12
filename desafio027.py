### Digitando uma cadeia de caracteres e retirando os espaços inuteis:
n = str(input('Digite seu nome completo')).strip()

### Transformando o nome em uma lista:
nome = n.split()
### Printando o primeiro indice que geralmente é o primeiro nome da pessoa:
print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
### Precisa tirar o -1 pra não contar o último nome:
print('Seu último nome é {}'.format(nome[len(nome) - 1]))
