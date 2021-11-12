### HERANÇA EM PYTHON

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        ### Diferenciando a classe!
        print(f'{self.nomeclasse} Falando!')

### SUBCLASSES:
class Cliente(Pessoa):

    def comprar(self):
        ### Diferenciando a classe!
        print(f'{self.nomeclasse} Comprando!')


class Aluno(Pessoa):
    def estudar(self):
        ### Diferenciando a classe!
        print(f'{self.nomeclasse} Estudando!')

class ClienteVIP(Cliente):
    ### CHAMANDO UM MÉTODO CONSTRUTOR DE UMA CLASSE PAI:
    def __int__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
    ### SOBREESCREVENDO UM MÉTODO DA CLASSE MÃE/SOBREPOSIÇÃO:
    def falar(self):
        ### BUSCA MÉTODO DA SUPER CLASSE:
        # super().falar()
        ### INFORMANDO DE QUAL CLASSE PAI BUSTAR O MÉTODO ESPECIFICO:
        Pessoa.falar(self)
        print('Outra coisa qualquer!')


