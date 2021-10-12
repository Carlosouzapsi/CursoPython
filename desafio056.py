somaIdades = 0
maiorIdade = 0
menorIdade = 0
nomeMaisVelho = ''
media = 0
totMulher20 = 0
for i in range(1, 5):
    print('=' * 20)
    print('      PESSOA {}'.format(i))
    print('=' * 20)
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('DIgite o sexo da pessoa M ou F: ')).upper().strip()
    somaIdades+=idade
    if i == 1 and sexo in 'M':
        maiorIdade = idade
        nomeMaisVelho = nome
    if sexo in 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeMaisVelho = nome
    if sexo in 'F' and idade < 20:
        totMulher20+=1

media = somaIdades / 4
print('A média de idades do grupo é: {}'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nomeMaisVelho, maiorIdade))
print('O total de mulher com menos de 20 anos é {}'.format(totMulher20))




