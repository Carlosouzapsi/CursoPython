lista1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lista2 = [160, 11, 50, 22, 43, 24, -12, 24, 542, 217]
lista3 = list()

lista2.reverse()  ### INVERTE OS VALORES DA LISTA 2

### SOMA DOS ELEMENTOS:
soma = lambda lista1, lista2: [lista1[ind] + lista2[ind] for ind in range(0, 10)]  # uso da F pra somar as listas.

result = soma(lista1, lista2)
# print(result)
lista3.append(result)
print(lista3)
