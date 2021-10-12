from datetime import date

anoNascimento = int(input('Digite o ano de nascimento do jovem: '))
anoAtual = date.today().year

idade = anoAtual - anoNascimento

if idade <= 9:
    print('Nadador pertence a categoria mirim.')
elif idade > 9 and idade <= 14:
    print('Nadador pertence a categoria infantil')
elif idade > 14 and idade <= 19:
    print('Nadador pertence a categoria Junior.')
elif idade > 19 and idade <= 25:
    print('Nadador pertence a categoria Sênior.')
elif idade > 25:
    print('Nadador pertence a categoria MASTER')