'''
Encapsulamento e Abstração

Encapsulamento - Em POO ocorre o encapsulamento do código das classes.
Objetivo é promover mais segurança no sistema. Agrupamento de métodos e atributos.
Com o encapsulamento é possível realizar a abstração

Abstração - Disponibilização ao usuário somente de métodos e atributos realmente
necessários de serem apresentados. Métodos e atributos privados permanecem ocultos.
'''

class Jogo:

    nivel = 8

    def __init__(self, forca, magia, resistencia):
        self.__forca = forca
        self.__magia = magia
        self.__res = resistencia
        self.__nivel = Jogo.nivel

    def atacar_raio(self):
        self.__res -= 5
        self.__magia -= 10

    def atacar_soco(self):
        self.__res -= 10
        self.__forca -= 10
    def __pular_nivel(self):
        Jogo.nivel += 1
        self.__nivel = Jogo.nivel

    def exercicio(self):
        self.__res += 5
        self.__forca += 10

    def status(self):
        print(f'Força: {self.__magia} Magia: '
              f'{self.__magia} Resistencia: {self.__res} Nivel: {self.__nivel}')



player1 = Jogo(76, 95, 88)

player1.status()
player1.atacar_raio()

player1.atacar_soco()
player1.status()

player1.exercicio()
player1.status()

# player1.pular_nivel()
# player1.status()




