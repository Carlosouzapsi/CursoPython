import math

class FormaGeometrica:
    def __init__(self, figura):
        self.__figura = figura

    def calcula_area(self):
        if self.__figura == 'quadrado':
            print(f"Área do quadrado: {float(input('Lado do quadrado: ')) ** 2} m")
        elif self.__figura == 'circulo':
            print(f"Área do círculo: {(float(input('Raio do círculo: ')) ** 2) * math.pi} m")

class AreaQuadrado(FormaGeometrica):

    def calcula_area(self):
        print(f"Área: {float(input('Lado do quadrado: ')) ** 2} m")

class AreaCirculo(FormaGeometrica):

    def calcula_area(self):
        print(f"Área: {(float(input('Raio do círculo: ')) ** 2) * math.pi:.2f} m")

quadrado = AreaQuadrado('quadrado')
quadrado.calcula_area()

circulo = AreaCirculo('circulo')
circulo.calcula_area()

