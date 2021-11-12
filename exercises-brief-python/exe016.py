import math
from math import pi

raio = int(input('Informe o raio do círculo: '))

def calcArea(r):
    pi = math.pi
    area = pi * math.pow(r, 2)
    return area

def calcVolume(r):
    pi = math.pi
    volume = (4 * pi * math.pow(r, 3)) / 3
    return volume

print(f'AREA: {calcArea(raio):.2f}')
print(f'VOLUME: {calcVolume(raio):.2f}')

