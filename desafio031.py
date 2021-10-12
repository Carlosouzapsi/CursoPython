distancia = float(input('Digite a distância de sua viagem:'))
print('Você está prestes a começar uma viagem de {} km'.format(distancia))
### Caso tenha desconto cai no if:
# precoPassagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45
### forma ternária:
### forma normal:
if distancia > 200:
    precoPassagem = 0.45 * distancia
else:
    precoPassagem = 0.50 * distancia
print('O preço da sua passagem é de R$ {:.2f}'.format(precoPassagem))

