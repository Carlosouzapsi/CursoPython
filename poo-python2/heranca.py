'''
Herança

- Aumentar o alcance de nossas classes utilizando menos código
- Se uma classe herda de outra classes, ela passa a herdar todos os atributos
  e métodos da classe herdada.

A classe herdada é conhecida como:
    Classe Mãe
    Classe Pai
    Classe Base
    Classe genérica
    Super Classe
Classe que herda é conhecida como:
    Classe Filha
    Classe Especifica
    Sub Classe
'''
class Aparelho:
    def __init__(self, marca, peso, volume):
        self.__marca = marca
        self.__peso = peso
        self.__volume = volume
    def volume(self):
        return f'O volume está em {self.__volume}'


class Televisao(Aparelho):
    def __init__(self, marca, peso, volume, polegadas):
        super().__init__(marca, peso, volume)
        self.__marca = marca
    ## Sobreescrita do método da classe mãe:
    def volume(self):
        ## chamada igual a da classe mãe:
        print(super().volume())
        return f'Olha só, {super().volume()}'

class Radio(Aparelho):
    def __init__(self, marca, peso, volume, frequencia):
        super().__init__(marca, peso, volume)
        self.__frequencia = frequencia


tv = Televisao('LG', 2.5, 80, 52)
radio = Radio('Sony', 1, 75, 105)

print(tv.volume())
print(radio.volume())

### MÉTODO SUPER PODE ACESSAR QUALQUER ATRIBUTO OU MÉTODO DA SUPER CLASSE!

### OVERRIDING: Reescrever um método na classe filha de uma classe mãe
