"""
- Para tratar erros em Python, é muito bom prestar
  Atenção na mensagem apresentada no console
  
  Erros mais comuns:
  
  a)AttributeError: Ocorre quando há falha de atribuição!
  Ex:
  
dicionario = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro'}
dicionario.add('ES') ## erro attribute método add. só funciona em cojuntos

b)IndexError: Ocorre quando não existe o indice de acesso dentro da variável
Ex:

list = [1,2,3,4,5]
print(lista[6]) ### dá erro pq não tem na lista o indice 6. não está no range'

c)KeyError: Acontece quando uma chave n é encontrada dentro de um dicionario:
Ex:
dicionario = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro'}
print(dicionario['SP'])
print(dicionario['MG'])  ### chave n existe no dicionario, por isso da keyerror

d)NameError: Ocorre quando uma variável ou função não é encontrada no código
Ex:

print(programandoIdeias) ### não está definido, programando ideias, precisa declarar

e)SyntaxError: Surge quando há um erro de sintaxe. O python não entende
ex:

break ## palavra declarada sozinha sem saber-se o que é isso no codigo fonte
def variavel = 5 ### sintaxe errada ao declada uma function em python

f)IndentationError: Ocorre quando há um erro de indentação no código
Ex:

x = 10
if x == 10:
x =5 ### Acusa o erro pq o código precisa estar corretamente indentado

g)TypeError: Ocorre quando há operação entre tipos incorretos

nome = 'carlos'
numero = 100
nome_numero = nome + numero 

h)ValueError: Acontece quando uma função recebe um parâmetro de tipo certo, mas
valor inválido.

valor = int(input('Digite um numero de 1 a 10: ')) ## informar uma string dará o erro
"""








