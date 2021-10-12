from datetime import date
atual = date.today().year
# nasc = int(input('Em que ano a pessoa nasceu? '))

somaMenores = 0
somaMaiores = 0
for c in range(1, 3):
    nasc = int(input('Em que ano a {}o pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade < 21:
        somaMenores+=1
    else:
        somaMaiores+=1
print('O número de pessoas menores de idade registradas é: {}'.format(somaMenores))
print('O número de pessoas menores de idade registradas é: {}'.format(somaMaiores))



