# #### UTILIZANDO O REDUCE:
#
# # 1 MODO FÁCIL USANDO O FATORIAL:
#
# n = int(input('Fator de: '))
# fat = 1
# for i in range(1, n + 1):
#     fat *= i
# print(fat)
#
# # 2 USANDO O REDUCE:
# from functools import reduce  # PRECISA SER IMPORTADO NAS VERSÕES MAIS NOVAS DO PYTHON
# lista = [1]
#
# lista.extend(range(1, n + 1))
#
# fat = reduce(lambda x, y: x * y, lista)
# print(fat)

##### UTILIZANDO O MAP:
import math

lista_pessoas = list()
cont = 1
while True:
    while True:
        try:
            peso = float(input('Informe o peso da pessoa em KG: '))
        except ValueError:
            print('O Valor digitado precisa ser um número real.')
        else:
            break
    while True:
        try:
            altura = float(input('Informe a Altura da pessoa em metros: : '))
        except ValueError:
            print('O Valor digitado precisa ser um número real.')
        else:
            break

    opt = str(input('Deseja informar os dados de mais pessoas? [S/N]: ')).upper().strip()[0]
    tupla_dados_pessoas = (peso, altura)
    lista_pessoas.append(tupla_dados_pessoas)
    if 'N' in opt:
        # print(lista_pessoas)
        cont += 1
        print('PROGRAMA ENCERRADO PELO USUÁRIO!')
        break


def calc_imc(imc_calc):
    imc_calc = (imc_calc[0] / math.pow(imc_calc[1], 2))
    return imc_calc


### USANDO O MAP PARA FAZER O CALCULO:
imc = map(calc_imc, lista_pessoas)
resultIMC = []
resultadoIMC = list(imc)

for num in resultadoIMC:
    resultIMC.append(round(num))

print(f'Lista total de IMCs: {resultIMC}')
# ### FILTER
sobrepeso = filter(lambda imc: imc > 25, resultIMC)
print(f'pessoas da lista com sobrepeso: {list(sobrepeso)}')
