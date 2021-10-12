resp = 'S'
media = 0
soma = 0
qtdValores = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma+=num
    qtdValores+=1
    if qtdValores == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0] ### ler e pegar somente o index da primeira letra
media = soma / qtdValores
print('Você digitou {} números, e a média foi {}'.format(qtdValores, media))
print('O  maior valor foi {} e o menor valor foi {}'.format(maior, menor))