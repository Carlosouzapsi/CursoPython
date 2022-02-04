# ### PORTÃO 1:
# portao1 = (29, 54, 45)
# cont = 0
# ### converter a tupla para uma lista:
# senha1 = list(portao1)
# cont = 0
# for num in portao1:
#     senha1[cont] = 0
#     cont+=1
# portao1 = tuple(senha1)
# print(f'Senha do portão 1: {portao1}')

### PORTÃO 2:
# portao2 = (12, 28, 37, 54)
# print(portao2)
# ### LEMBRAR QUE COMEÇA A CONTAGEM PELO INDICE ZERO!
# elemento2 = portao2[1]
# elemento3 = portao2[2]
# soma1 = elemento2 + elemento3
# elemento1 = portao2[0]
# elemento4 = portao2[3]
# soma2 = elemento1 + elemento4
# senha2 = (soma1, soma2)
# print(senha2)

### PORTÃO 3:
portao3 = (16, 86, 78, 32, 85, 12)
valor_min = min(portao3)
print(valor_min)
valor_max = max(portao3)
print(valor_max)
senha3 = (valor_min, valor_max)
print(senha3)
