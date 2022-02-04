linhas_aereas = ['Azul', 'Gol', 'Avianca']
voo_1 = [115,95,110]
voo_2 = [195,80,225]


voos1e2 = zip(voo_1, voo_2)
maxPass = map(lambda voos: max(voos), voos1e2) ## valor max de pass por companhia



listaMaxPass = list(maxPass)

compMax = zip(linhas_aereas, listaMaxPass)

listaCompMax = list(compMax)

umaEst = list(filter(lambda valMax: valMax[1] <= 100, listaCompMax))

duasEst = list(filter(lambda valMax: valMax[1] > 100 and valMax[1] <= 200, listaCompMax))

tresEst = list(filter(lambda valMax: valMax[1] > 200 and valMax[1] <= 300, listaCompMax))

print(f'Uma estrelas:  {umaEst[0][0]} - {umaEst[0][1]}')
print(f'Duas estrelas: {duasEst[0][0]} - {duasEst[0][1]}')
print(f'Três estrelas: {tresEst[0][0]} - {tresEst[0][1]}')

### Dica, realizar vários prints ao longo do código pode ajudar a entender a lógica aplicada!
