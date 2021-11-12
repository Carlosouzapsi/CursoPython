class Escritor:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo!')

class MaquinaEscrever:
    def escrever(self):
        print('Máquina está sendo usada!')
