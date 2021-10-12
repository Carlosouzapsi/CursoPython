### Informando a string com os caracteres "inuteis" retirados:
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em maiúsculas é {nome.lower()}')
tirandoEspacos = nome.count(' ')
print(f'Possui ao todo {len(nome) - tirandoEspacos} letras')
letrasPrimeiroNome = nome.find(' ')
print(f'Seu primeiro nome tem {letrasPrimeiroNome} letras')

### outra forma
separa = nome.split()
print(f'Seu primeiro nome tem {len(separa[0])} letras')