"""

SORTED E REVERSED


SORTED: semelhante ao sort. Porém, serve para qualquer iterável diferente do sort
        que é só para listas
        
REVERSED: Semelhante ao reverse. Porém, reverse é utilizando apenas em listas,
Reversed pode ser usado em qualquer iterável
"""
### Exemplo de sorted em lista:

# notasL = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
# print(sorted(notasL))

# ### Exemplo de sorted em tupla:
# notasT = (10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3)
# print(sorted(notasT))

# ### Exemplo de sorted em conjuntos:
# notasC = {10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3}
# print(sorted(notasC)) #### Em conjuntos o sorted não deixa repetir os valores

# ### Invertendo o sorted:
# print(sorted(notasT, reverse=True))


### Exemplos de Reversed (não ordena, apenas inverte)
# notasL = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
# print(reversed(notasL)) #### Imprime um endereço de memória apenas n]ao confundir com sorted
# print(list(reversed(notasL))) ### imprime os valores se converter para lista

# ### Exemplo de Reverse em tupla:
# notasT = (10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3)
# print(reversed(notasT))
# print(list(reversed(notasT)))

# ### Exemplo de Reversed em conjuntos: Não funciona o reversed, não possui nenhum tipo de ordenação dos dados
# notasC = {10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3}
# print(list(reversed(notasC))) ### Type Error

### Iterando um reversed
notasL = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
for nota in reversed(notasL):
        print(nota, end=' ') ### retorno de um objeto iterator com elementos invertidos!






