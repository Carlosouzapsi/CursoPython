import math

altura = float(input('Informe a altura em m: '))
aceleracao = 9.8
def calcDist(a):
    vi = 0
    vf = math.sqrt(math.pow(vi, 2) + 2 * aceleracao * a)
    return vf

print(f'A velocidade final é {calcDist(altura):.2f} m/s')