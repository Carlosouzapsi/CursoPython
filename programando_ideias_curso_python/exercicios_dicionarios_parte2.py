flores = {'Rosas Vermelhas': 145.00, 'Girassóis': 125.00, 'Margaridas': 120.00,
          'Flores do Campo': 140.00}
presentes = {'Urso de Pelúcia': 55.00, 'Caixa de Bombom': 60.00, 'Colar': 75.00,
             'Roupas': 40.00}
lugares = {'Praia': 70.00, 'Sair para jantar': 150.00, 'Parque de diversões': 170.00,
           'Hotel': 180.00}

### Combinação mais cara:
preco_total = 0
flor_cara = ''
presente_caro = ''
lugar_caro = ''

for flor, valor in flores.items():
    for presente, preco in presentes.items():
        for lugar, custo in lugares.items():
            preco_atual = valor + preco + custo
            if preco_atual > preco_total:
                preco_total = preco_atual
                flor_cara = flor
                presente_caro = presente
                lugar_caro = lugar

print(f'Custo total: {preco_total}, Flor: {flor_cara}, Presente: {presente_caro}, Lugar: {lugar_caro}')

### ENCONTRANDO A COMBINAÇÃO MAIS BARATA:

### Combinação mais barata:
aux = 0
preco_total = 0
flor_barata = ''
presente_barato = ''
lugar_barato = ''

for flor, valor in flores.items():
    for presente, preco in presentes.items():
        for lugar, custo in lugares.items():
            if aux == 0:
                preco_total = valor + preco + custo
                aux += 1
            else:
                preco_atual = valor + preco + custo
                if preco_atual < preco_total:
                    preco_total = preco_atual
                    flor_barata = flor
                    presente_barato = presente
                    lugar_barato = lugar

print(f'Custo total: {preco_total}, Flor: {flor_barata}, Presente: {presente_barato}, Lugar: {lugar_barato}')

### ACHANDO A MÉDIA OPÇÃO DE PREÇO:
preco_total = 0
list = []

for flor, valor in flores.items():
    for presente, preco in presentes.items():
        for lugar, custo in lugares.items():
            list.append(valor + preco + custo)
list.sort()  # organiza a lista do menor para o maior elemento
preco_total = list[(len(list) // 2)]  ### pego o termo central

for flor, valor in flores.items():
    for presente, preco in presentes.items():
        for lugar, custo in lugares.items():
            if valor + preco + custo == preco_total:
                print(f'Custo total: {preco_total}, Flor: {flor}, Presente: {presente}, Lugar: {lugar}')
