nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota:  '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('O aluno foi reprovado!')
elif media >= 5.0 and media <= 6.9:
    print('O aluno estão em recuperação!')
elif media >= 7.0:
    print('O aluno foi aprovado!')