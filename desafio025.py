### Eliminando os espaços inúteis com strip:
nomeCompleto = str(input('Digite o seu nome completo:')).strip()
nomeCompleto = nomeCompleto.upper()
### utilizando o operador in para fazer essa verificação:
print('Seu nome contém Silva? {}'.format('SILVA' in nomeCompleto))

