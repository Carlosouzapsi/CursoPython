aluno = dict()
for c in range(0, 1):
    aluno['nome'] = str(input('Nome do Aluno: '))
    aluno['media'] = float(input('Media de {}: '.format(aluno['nome'])))

for k, v in aluno.items():
    print('{} é igual: {}'.format(k, v))
if aluno['media'] >= 6.0:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('A situação é igual a {}'.format(aluno['situação']))



