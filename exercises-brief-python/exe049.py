ano = int(input('Ano: '))

def verifica_ano(a):
    animal = ' '
    if a % 12 == 8:
        animal = 'Dragão'
    if a % 12 == 9:
        animal = 'Cobra'
    if a % 12 == 10:
        animal = 'Cavalo'
    if a % 12 == 11:
        animal = 'Ovelha'
    if a % 12 == 0:
        animal = 'Macaco'
    if a % 12 == 1:
        animal = 'Galo'
    if a % 12 == 2:
        animal = 'Cachorro'
    if a % 12 == 3:
        animal = 'Porco'
    if a % 12 == 4:
        animal = 'Rato'
    if a % 12 == 5:
        animal = 'Boi'
    if a % 12 == 6:
        animal = 'Tigre'
    if a % 12 == 7:
        animal = 'Lebre'
    return animal

print(verifica_ano(ano))

