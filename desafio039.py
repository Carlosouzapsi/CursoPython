from datetime import date

anoNascimento = int(input('Digite o ano de nascimento do jovem: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print('Sua idade é: {} anos'.format(idade))
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
     tempoQueFalta = 18 - idade
     print('Ainda faltam {} anos para você se alistar'.format(tempoQueFalta))
elif idade > 18:
     print('Já passou do prazo para você se alistar.')