
lista = [23, 1, 12, 7.65]
tupla = (0, True, 0.54, 0, 54, True)

conjunto = {max(lista), min(lista), max(tupla), min(tupla)} 
# Conjunto contém os valores máximos e mínimos da lista e da tupla
print(conjunto)

print(any(conjunto)) ### Há pelo menos um valor verdadeiro no conjunto?
print(all(conjunto)) ### os valores do cojunto são verdadeiros


