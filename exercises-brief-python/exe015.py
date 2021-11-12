distancia = int(input('Informe a distância em metros: '))

def conversorKm(d):
    conver = d / 1000
    return conver

print(f'O valor {distancia} metros convertido para Km é {conversorKm(distancia):.2f}')


