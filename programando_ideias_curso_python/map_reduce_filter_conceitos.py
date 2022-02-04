# def maiorQ10(num):
#         if num > 10:
#             print('Maior')
#         else:
#             print('Menor')
#
# # maiorQ10(27)
# # maiorQ10(2)
#
# ### MUITOS VALORES PARA SEREM TESTADOS NA FUNÇÃO!
# numeros = [4, 6, 5, 91, 8, 7, 14, 16, 98, 4, 1.3, 75.4, 3]

### USANDO O MAP A TAREFA FICA MAIS SIMPLES: OBS: PRECISA ATRIBUIR O MAP A UMA VARIÁVEL!
# result = map(maiorQ10, numeros)
# # print(result) ### retorna o endereço de memória!
# # print(type(result)) ### retorna a class do tipo map!]
# print(list(result)) ### imprime a lista (forma correta de usar com o print)!

### MAP COM FUNÇÃO LAMBDA:
# nascimento = lambda dado: f'Ano de nascimento: {dado[0] - dado[1]}'
# ### DESCOBRI ANO DE NASC PASSANDO O ANO 'ATUAL' E A IDADE:
# dados = [(1998, 22), (1815, 88), (2027, 3)]
# print(list(map(nascimento, dados)))

### FILTER, MESMA SINTAXE DO MAP POREM FILTRA DADOS DE UMA FUNC OU COLEÇÃO
# numeros = [1, 4, 1, 3, 5, 6, 3, 2, 9, 7, 3, 6, 9]
# result = filter(lambda num: num > math.pi, numeros) ## ULTIMO PARAM É UM RETORNO!
# ### OBS -> TRADUZINDO A FUNÇÃO LAMBDA EM UMA EXPRESSÃO DE FUNÇÃO COMUM:
# # def qualquer(*args):
# #     if num in args:
# #         if num > math.pi:
# #             return True
# #         else:
# #             return False
#
# # print(result) END DE MEMORIA
# # print(type(result)) DADO DO TIPO FILTER
#
# print(list(result)) ## MAIORES QUE PI!
# print(list(result)) ## VALOR SE PERDE APÓS UTILIZAÇÃO

### USANDO FILTER COM MAP
# numeros = [1, 4, 1, 3, 5, 6, 3, 2, 9, 7, 3, 6, 9]
# # POR PARTES:
# ## FILTER:
# filter(lambda num: num % 2 == 0, numeros)
#
# ## MAP:
# map(lambda n: n ** 2, filter(lambda num: num % 2 == 0, numeros))
#
# ## ULTIMA PARTE:
# result = list(map(lambda n: n ** 2, filter(lambda num: num % 2 == 0, numeros)))
# print(result)

### REDUCE - RELACIONA DADOS POSTERIORES DE UMA COLEÇÃO COM O RESULTADO DE UMA RELAÇÃO JÁ FEITA:
### PYTHON 3+ - PRECISA IMPORTAR A FUNC RESULT, DO MODULO FUNCTOOLS

### EXEMPLOS DE REDUCE

# from functools import reduce
#
# numeros = [2, 1, 2, 3]
# ### UTILIZAR REDUCE APENAS SE FOR NECESSÁRIO DEVIDO A IDEIA 'CONFUSA' DA FUNÇÃO!
# ### USAR UM LOOP FOR É MAIS LEGÍVEL NA MAIOR PARTE DAS VEZES!
# result= reduce(lambda x, y: x ** y, numeros)
# print(result)
