class Objetos:
    def __init__(self, videogame, senhacelular, dinheiro, camisa, livro):
        self.__videogame = videogame
        self.__senhacelular = senhacelular
        self.__dinheiro = dinheiro
        self.__camisa = camisa
        self.__livro = livro

    @property
    def videogame(self):
        return f'Videogame: {self.__videogame}'

    @property
    def senhacelular(self):
        return f'Senhacelular: {self.__senhacelular}'

    @property
    def dinheiro(self):
        return f'Dinheiro: {self.__dinheiro}'

    @property
    def camisa(self):
        return f'Camisa: {self.__camisa}'

    @property
    def livro(self):
        return f'Livro: {self.__livro}'

    @videogame.setter
    def videogame(self, videogame):
        self.__videogame = videogame

    @senhacelular.setter
    def senhacelular(self, senhacelular):
        self.__senhacelular = senhacelular

    @dinheiro.setter
    def dinheiro(self, dinheiro):
        self.__dinheiro = dinheiro

    @camisa.setter
    def camisa(self, camisa):
        self.__camisa = camisa

    @livro.setter
    def livro(self, livro):
        self.__livro = livro


objeto1 = Objetos('Sega Saturno', '12345', 10.0, 'Calvin Klein', 'Harry Podre')

#### Acessando o atributo video game por causa do setter:
print(objeto1.videogame)
### Modificando o valor do atributo videogame:
objeto1.videogame = 'Playstation'
print(objeto1.videogame)








