'''
Herança múltipla

- Uma classe pode herdar múltiplas classes ao mesmo tempo.

- Existem dois tipos de herança múltipla: Direta e Indireta.

- Independente do tipo, a Sub Classe herda todos os métodos e atributos das Super Classes.
'''
## Herança múltipla direta:

# class Energia:
#     def __init__(self, ligado):
#         self.__ligado = ligado
#
#     @property
#     def ligado(self):
#         return self.__ligado
#
#     def botao(self):
#         self.__ligado = not self.__ligado
#
# class Memoria:
#
#     def __init__(self, ram):
#         self.__ram = ram
#
#     @property
#     def ram(self):
#         return self.__ram
#
#
# class Monitor:
#
#     def __init__(self, polegadas):
#         self.__polegadas = polegadas
#
#     @property
#     def polegadas(self):
#         return self.__polegadas
#
# class Computador(Energia, Memoria, Monitor):
#
#     def __init__(self,ligado, ram, polegadas, valor):
#         Energia.__init__(self, ligado)
#         Memoria.__init__(self, ram)
#         Monitor.__init__(self, polegadas)
#         self.__valor = valor
#
#     @property
#     def valor(self):
#         return self.__valor
#
#
# meuPC = Computador(True, 8, 15.6, 3200)
# print(meuPC.ram)
# print(meuPC.polegadas)
# print(meuPC.valor)
# print(meuPC.ligado)
# meuPC.botao()
# print(meuPC.ligado)

### Herança multipla indireta:

# class Energia:
#
#     def __init__(self, ligado):
#         self.__ligado = ligado
#
#     @property
#     def ligado(self):
#         return self.__ligado
#
#     def botao(self):
#         self.__ligado = not self.__ligado
#
# class Memoria(Energia):
#
#     def __init__(self, ligado, ram):
#         super().__init__(ligado)
#         self.__ram = ram
#
#     @property
#     def ram(self):
#         return self.__ram
#
# class Monitor(Memoria):
#
#     def __init__(self, ligado, ram, polegadas):
#         super().__init__(ligado, ram)
#         self.__polegadas = polegadas
#
#     @property
#     def polegadas(self):
#         return self.__polegadas
#
# class Computador(Monitor):
#
#     def __init__(self, ligado, ram, polegadas, valor):
#         super().__init__(ligado, ram, polegadas)
#         self.__valor = valor
#
#     @property
#     def valor(self):
#         return self.__valor
#
# meuPC = Computador(True, 8, 15.6, 3200)
# print(meuPC.ram)
# print(meuPC.polegadas)
# print(meuPC.valor)
# print(meuPC.ligado)
# meuPC.botao()
# print(meuPC.ligado)
#
# ### Conferindo as instâncias:
# print(f'meuPC é do tipo Energia? {isinstance(meuPC, Energia)}')


#### MRO - METHOD RESOLUTION ORDER
class Estado:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f'Eu sou {self.nome} e estou em algum estado por aí'

class Bahia:
    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):
        return f'Eu sou {self.nome} e estou na Bahia'

class Alagoas(Estado):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):
        return f'Eu sou {self.nome} e estou no Alagoas'

class Nordeste(Bahia, Alagoas):
    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):
        return f'Eu sou {self.nome} e estou no Nordeste'

#### MÉTODO MÁGICO:
print(Nordeste.__mro__)
print(Nordeste.mro())
# print(help(Nordeste))













