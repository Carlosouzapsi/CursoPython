lista_nomes = ['Carlos', 'Paulo', 'Simone']
print(lista_nomes)

nota_p1 = [23, 78, 32]
nota_p2 = [34, 10, 45]
nota_p3 = [12, 0, 99]

listaNotas = []

tabela = zip(nota_p1, nota_p2, nota_p3)
for notas in tabela:
    listaNotas.append(sum(notas))

dicionario = zip(lista_nomes,listaNotas)

dicionario_final = dict(dicionario)

vencedor = ' '
pontos = 0

for part, pts in dicionario_final.items():
    print(f'Participante: {part}. Pontos: {pts}')
    if pts > pontos: ## ver. qual nota é maior
        pontos = pts
        vencedor = part

print(f'\n vencedor: {vencedor} - Pontos: {pontos}')
    