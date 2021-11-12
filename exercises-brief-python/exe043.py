c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88

nota = float(input('Informe a frequencia da nota: '))

if nota == c4:
    freq = 'c4'
elif nota == d4:
    freq = 'd4'
elif nota == e4:
    freq = 'e4'
elif nota == f4:
    freq = 'f4'
elif nota == g4:
    freq = 'g4'
elif nota == a4:
    freq = 'a4'
elif nota == b4:
    freq = 'b4'

print(f'A nota é: {freq}')