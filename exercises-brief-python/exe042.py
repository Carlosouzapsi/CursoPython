c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88

nome = str(input('Informe a nota a ser analisada: '))
nota = nome[0].upper()
oitava = int(nome[1])

if nota == "C":
    freq = c4
elif nota == "D":
    freq = d4
elif nota == "E":
    freq = e4
elif nota == "F":
    freq = f4
elif nota == "G":
    freq = g4
elif nota == "A":
    freq = a4
elif nota == "B":
    freq = b4

freq = freq / 2 ** ( 4 - oitava)
print(f'A frequencia da nota {nome} é {freq}')





