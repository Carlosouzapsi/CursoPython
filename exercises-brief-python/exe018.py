import math

altura = int(input('Informe a altura do cilindro em cm: '))
raio = int(input('Informe o raio da base do cilindro: '))

def calcVolume(a, r):
    volume = math.pi * math.pow(r, 2) * a
    return volume

