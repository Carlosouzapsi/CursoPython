class Personagem:
    def __init__(self, nome, altura, peso, resistencia):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.res = resistencia

    def poder(self, magia, persuasao, agilidade, forca):
        self.__magia = magia
        self.__persuasao = persuasao
        self.__agilidade = agilidade
        self.__forca = forca
        self.__soma = self.__magia + self.__persuasao + self.__agilidade + self.__forca
        return self.__soma

dict_poder = {}

p1 = Personagem('Carlos', 1.76, 95, 30)
dict_poder[p1.nome] = p1.poder(100, 50, 300, 200)

p2 = Personagem('Souza', 1.80, 100, 30)
dict_poder[p2.nome] = p2.poder(10, 20, 2, 0)

p3 = Personagem('Otavio', 1.99, 200, 30)
dict_poder[p3.nome] = p3.poder(100, 20, 27, 15)

### Imprimindo o dicionário:
print(dict_poder)
# print(p1.__dict__) # Retorna um dicionário com todos os atributos de cada objeto!
# print(p2.__dict__)
# print(p3.__dict__)

maior = 0
nome = ''

for chave, valor in dict_poder.items():
    if maior < valor:
        maior = valor
        nome = chave
print(f'O mais forte: {nome} com {maior} pontos de poder.')





