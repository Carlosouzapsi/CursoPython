nome = str(input('Qual é o seu nome?'))
### Condição composta:

# if nome == 'Carlos':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
#     print('Bom dia, {}!'.format(nome))

### Condição simples:
# if nome == 'Carlos':
#     print('Que nome lindo você tem!')
# print('Bom dia, {}!'.format(nome))

### Mais exemplos:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi {:1.f}'.format(media))
if media >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! estude mais!')

