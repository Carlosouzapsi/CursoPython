### SETTER = CONFIGURANDO UM VALOR ( = )
### GETTER = OBTER UM VALOR ( .atributo )

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    ### GETTER:
    @property
    def nome(self):
        return self.__nome
    ### SETTER:
    @nome.setter
    def nome(self, nome):
        self.nome = nome




p1 = Pessoa('Carlos')
print(p1.nome)

