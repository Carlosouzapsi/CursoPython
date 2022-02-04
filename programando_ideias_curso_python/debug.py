import pdb
"""
PARA DEBUGAR PROGRAMAS EM PYTHON:
1)Importar a biblioteca com o método pdb
2)Utilizar o método set_trace() e posicioná-lo aonde quiser no código
3)Utilizar as palavras chaves:
- l(list): Apresenta onde você está no código ( p  x) -> x é a variável que se lista
- n(next): Pular para a próxima linha
- p(print): imprime uma variável
- c(continue): Continua a execução do código até o final do programa ou até o
  próximo set_trace()
- cuidado ao usar letras no código que se confundem com os comandos!
- pdb n precisa ser importado em versões da 3.7 em diante, foi incorporado
  na built-in do python co nome breakpoint()
"""
x = 2
y = 3
# breakpoint() ### declaração do breakpoint inicio
z = x * y
nome = 'Clara'
frase = nome * z
print(frase)

# breakpoint() ### final