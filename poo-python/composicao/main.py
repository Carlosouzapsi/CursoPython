from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
print(cliente1.nome)
cliente1.insere_endereco('Belo Horizonte', 'MG')
cliente1.lista_enderecos()
print()
### SERÁ APAGADO O CLIENTE E TAMBÉM SEU ENDEREÇO, ACONTECE PROS DEMAIS TAMBÉM!!!
del cliente1
print()

cliente2 = Cliente('Maria', 52)
print(cliente2.nome)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 56)
print(cliente3.nome)
cliente3.insere_endereco('São Paulo', 'SP')

print('########################################')
