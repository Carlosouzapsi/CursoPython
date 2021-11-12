# c1,qtd1,preco1 = input().split(" ") # pega 3 valores na mesma linha e atribui a variáveis
# c2,qtd2,preco2 = input().split(" ") # pega 3 valores na mesma linha e atribui a variáveis
# # Converte o valor para os tipos necessários
# c1 = int(c1)
# qtd1 = int(qtd1)
# preco1 = float(preco1)
# c2 = int(c2)
# qtd2 = int(qtd2)
# preco2 = float(preco2)
# total = (qtd1 * preco1) + (qtd2 * preco2)
# print(f"VALOR A PAGAR: R$ {total}")

c1,qtd1,preco1 = input().split(" ")
c2,qtd2,preco2 = input().split(" ")

c1 = int(c1)
qtd1 = int(qtd1)
preco1 = float(preco1)
c2 = int(c2)
qtd2 = int(qtd2)
preco2 = float(preco2)
total = (qtd1 * preco1) + (qtd2 * preco2)
print(f"VALOR A PAGAR: R$ {total:.2f}")


