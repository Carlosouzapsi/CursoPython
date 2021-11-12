letra = str(input('Digite uma letra: ')).strip()[0]

def id_letra(l):
    vogal = f'A letra {l} é vogal'
    consoante = f'A letra {l} é uma consoante'
    if 'a' in letra or 'e' in letra or 'i' in letra or 'o' in letra or 'u' in letra:
        return vogal
    else:
        return consoante

print(id_letra(letra))