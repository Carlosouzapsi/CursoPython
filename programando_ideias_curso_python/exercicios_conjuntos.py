estados_dudu = {'ES', 'SP'}
estados_sami = {'RJ', 'BA'}

print('Dudu visitou:')
for estados in estados_dudu:
    print(estados)
print('Sami visitou:')
for estados in estados_sami:
    print(estados)

print('6 MESES DEPOIS...')
# esportes.add('Futsal') #Para usar: variavel.add(elemento a ser adicionado)
cont = 0
estado_dudu_input = ""
while True:
    estado_dudu_input = str(input('Informe o estado que dudu visitou: '))
    if estado_dudu_input != "":
        estados_dudu.add(estado_dudu_input)
    else:
        print('Adicionar novo estado para o dudu encerrado com sucesso!')
        break
# estados_dudu2 = {'BA', 'AC', 'SC', 'SE'}
# estados_dudu_final = estados_dudu.union(estados_dudu2)
print('Dudu visitou: ')
for estados in estados_dudu:
    print(estados)

estados_sami_input = ""
while True:
    estados_sami_input = str(input('Informe o estado que sami visitou: '))
    if estados_sami_input != "":
        estados_sami.add(estados_sami_input)
    else:
        print('adcionar novo estado para sami encerrado com sucesso!')
        break
# estados_sami2 = {'BA', 'MG', 'AM', 'PR'}
# estados_sami_final = estados_sami.union(estados_sami2)
print('Sami visitou: ')
for estados in estados_sami:
    print(estados)

print(f'Os estados que dudu visitou e sami não visitou são: {estados_dudu.difference(estados_sami)}')
print(f'Estados que os dois visitaram: {estados_dudu.intersection(estados_sami)}')
estados_visitados = estados_dudu.union(estados_sami)
print(f'Foram visitados: {len(estados_visitados)} estados.')
perc = 100 * len(estados_visitados) / 27
print(f'O percentual de estados do Brasil que foram visitados é: {perc:.2f} %')
if len(estados_sami) > len(estados_dudu):
    print(f'Sami ganhou e visitou {len(estados_sami) * 100 // 27}%')
elif len(estados_dudu) > len(estados_sami):
    print(f'Dudu ganhou e visitou {len(estados_sami) * 100 // 27}%')
else:
    print('Empatou!')
