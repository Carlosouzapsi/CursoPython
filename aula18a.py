# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# ### Precisa fazer cópias da estrutura primeiro!!!!
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# ### Precisa fazer cópias da estrutura primeiro!!!!
# galera.append(teste[:])
# print(galera)

# galera = [['João', 19],['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# ### Só o João:
# print(galera[0])
# ### Só o nome do joão:
# print(galera[0][0])
#
# for p in galera:
#     # print(p, end='')
#     print(p[0], end=' ')

galera = list()
dado = list()
totmaior = 0
totmenor = 0
for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print('É maior de idade: {}'.format(p[0]))
        totmaior+=1
    else:
        print('É menor de idade {}'.format(p[0]))
        totmenor+=1

print('Temos {} maiores de idade e {} menores de idade.'.format(totmaior, totmenor))