maiores = 0
homens = 0
mulherMenor20 = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa: [M/F]: ')).strip().upper()[0]

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        maiores+=1
    if sexo == 'M':
        homens+=1
    if sexo == 'F':
        if idade < 20:
            mulherMenor20 +=1
    if continuar == 'N':
        break

print('Existem {} pessoas maiores de 18 anos.'.format(maiores))
print('Foram cadastrados {} homens.'.format(homens))
print('Foram cadastradas {} mulheres com menos de 20 anos.'.format(mulherMenor20))



