from random import randint as ri

class Livro:
    def __init__(self, nome, qtd_pag, edicao, vendas):
        self.__nome = nome
        self.__qtd_pag = qtd_pag
        self.__edicao = edicao
        self.__vendas = vendas

    def __repr__(self):
        return f'Livro: Nome = {self.__nome} Edicao = {self.__edicao}'

    def __len__(self):
        return self.__qtd_pag

    def vendas(self):
        return self.__vendas

livro1 = Livro('Aprendendo Python', 150, 1, ri(0, 500000))
livro2 = Livro('O pequeno Príncipe', 200, 2, ri(0,500000))
livro3 = Livro('Mar Sem Fim', 300, 3, ri(0,500000))

print(livro1)
print(livro2)
print(livro3)

print(f'Livro 1: {len(livro1)} páginas.')
print(f'Livro 2: {len(livro2)} páginas.')
print(f'Livro 3: {len(livro3)} páginas.')

print(f'Arrecadação do livro 1: {livro1.vendas()}')
print(f'Arrecadação do livro 2: {livro2.vendas()}')
print(f'Arrecadação do livro 3: {livro3.vendas()}')

valorTotal = livro1.vendas() + livro2.vendas() + livro3.vendas()
if valorTotal > 100000:
    print('\nParábens! Você agora é um milionário!')
else:
    print('\nTente criar mais livros!')
print(f'Valor arrecadado: {valorTotal}')

