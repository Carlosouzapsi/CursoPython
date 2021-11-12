a,b,c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
#### A)
areaT = (a * c) / 2
print(f'TRIANGULO: {areaT:.3f}')
### B)
areaC = pi * (c * c)
print(f'CIRCULO: {areaC:.3f}')
### C)
areaTrap = ((a + b) * c) / 2
print(f'TRAPEZIO: {areaTrap:.3f}')
### D)
areaQ = b * b
print(f'QUADRADO: {areaQ:.3f}')
### E)
areaR = a * b
print(f'RETANGULO: {areaR:.3f}')

