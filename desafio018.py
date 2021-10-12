import math
angulo = float(input('Digite o ângulo que você deseja: '))
#### convertendo para radianos:
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
### imprimindo:
print(f'o angulo de {angulo} tem o seno {seno:.2f}')
print(f'o angulo de {angulo} tem o cosseno {cosseno:.2f}')
print(f'o angulo de {angulo} tem o tangente {tangente:.2f}')