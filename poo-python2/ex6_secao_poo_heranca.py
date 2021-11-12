class Controle:

    ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado

class ArCondicionado(Controle):
    def __init__(self, temperaturaAtual):
        self.__temperaturaAtual = temperaturaAtual

    def controle_temperatura(self, temperatura):
        self.__temperaturaAtual = temperatura

    @property
    def temperaturaAtual(self):
        return f'Temperatura atual: {self.__temperaturaAtual}'

class Microondas(Controle):
    def __init__(self, tempoAtual):
        self.__tempoAtual = tempoAtual

    def controle_tempo(self, tempo):
        self.__tempoAtual = tempo

    @property
    def tempoAtual(self):
        return f'Tempo atual: {self.__tempoAtual}'

class Televisao(Controle):

    def __init__(self, volumeAtual):
        self.__volumeAtual = volumeAtual

    def controle_volume(self, volume):
        self.__volumeAtual = volume

    @property
    def volumeAtual(self):
        return f'Volume atual: {self.__volumeAtual}'

arc = ArCondicionado(45)
mic = Microondas(60)
tv = Televisao(85)

print(arc.ligado)
arc.liga_desliga()
print(arc.ligado)
print(arc.temperaturaAtual)
arc.controle_temperatura(50)
print(arc.temperaturaAtual)
















