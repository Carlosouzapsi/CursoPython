class Animal:

    def andar(self):
        return f'Estou andando!'
    def correr(self):
        return f'Estou correndo!'

class Carnivoro(Animal):

    def cacarAnimal(self):
        return f'Estou caçando!'

    def comerCarne(self):
        return f'Comendo carne!'

class Herbivoro(Animal):

     def procurarArvore(self):
         return f'Procurando árvore!'

     def comerFolhas(self):
         return f'Comendo folhas!'

class Homem(Carnivoro, Herbivoro):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def lerLivro(self):
        return f'{self.__nome} está lendo livro!'

class Urso(Carnivoro, Herbivoro):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def hibernar(self):
        return f'{self.__nome} está hibernando!'

c1 = Homem('Carlos')
print(c1.nome)
print(c1.andar())
print(c1.correr())
print(c1.comerCarne())
print(c1.lerLivro())
u1 = Urso('Pooh')
print(u1.hibernar())
print(u1.comerFolhas())







