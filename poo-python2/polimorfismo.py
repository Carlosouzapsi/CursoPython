'''
Polimorfismo

- Significa muitas formas(poli - muitas; morfis - formas)

- Por exemplo, um overriding é uma representação de polimorfismo

'''
### Exemplo:

class Comida:

    def __init__(self, alimento):
        self.__alimento = alimento

    @property
    def alimento(self):
        return self.__alimento

    def apresentar(self):
        raise NotImplementedError('Esse método só funciona se sub classe implementá-lo(sobreescrevê-lo)')

class Fruta(Comida):
    def __init__(self, alimento):
        super().__init__(alimento)

    def apresentar(self):
        print(f'Sou uma fruta, você gosta de {self.alimento}')

class Carne(Comida):
    def __init__(self, alimento):
        super().__init__(alimento)

    ### Se deixar comentado dispara a exceção da classe mãe:
    # def apresentar(self):
    #     print(f'Sou uma carne, você goste de {self.alimento}')

fruta = Fruta('laranja')
fruta.apresentar()

carne = Carne('frango')
carne.apresentar()