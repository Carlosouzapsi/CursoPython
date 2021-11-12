### RELAÇÃO DE COMPOSIÇÃO: UMA CLASSE É DONA DE OBJETOS DE OUTRA CLASSE

### PRIMEIRA CLASSE:
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO!')

### SEGUNDA CLASSE:
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.estado}/{self.cidade} FOI APAGADO!')
