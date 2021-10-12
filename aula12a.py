### usando o strip pra retirar espaços inúteis:
nome = str(input('Qual é seu nome? ')).strip()
if nome == 'Carlos':
    print('Que nome bonito!')
elif nome == 'Pedro':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))