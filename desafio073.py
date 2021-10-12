brasileirao = ('Vasco', 'Flamengo', 'Avai', 'Figueirense', 'Chapecoense', 'Paraná', 'São Paulo')
##### IMPRIMINDO TUDO!
for t in brasileirao:
    print(t)
### A
print('Os 3 primeiros colocados são: {}'.format(brasileirao[:3]))

### B
print('Os últimos 3 colocados são: {}'.format(brasileirao[-3:]))

### C
print('Os times em ordem alfabética são {} : '.format(sorted(brasileirao)))

### D
print('O time da chapecoense está na {}a posição :'.format(brasileirao.index('Chapecoense') + 1))