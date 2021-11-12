class Pessoa:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, aumento):
        self.__salario+=aumento

class Funcionario(Pessoa):
    def promocao(self):
        self.salario *= 1.1

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, codigo, numEstagiarios, codigoEstagiarios):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo
        self.__numEstagiarios = numEstagiarios
        self.__codigoEstagiarios = codigoEstagiarios

    def trocar_codigo(self, novoCodigo):
        self.__codigoEstagiarios = novoCodigo

    def __repr__(self):
        return f'Sou o(a) gerente {self.nome}, recebo {(round(self.salario))} e reais e quero um café.'


class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario, codigo):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo

    def __repr__(self):
        return f'Sou o(a) estagiário {self.nome}, recebo {(round(self.salario))} reais e tenho que levar um café na administração.'


gerente = Gerente('Pablo', 12345678900, 12000, 'cod4433', 3, 'es1234')
estagiario1 = Estagiario('João', 12345678911, 400, 'es1234')
estagiario2 = Estagiario('Larissa', 12345678933, 400, 'es1234')
estagiario3 = Estagiario('Pedro', 12345678944, 400, 'es1234')

print(gerente.__repr__())
print(estagiario1.__repr__())

print('\n')
estagiario1.promocao()
estagiario2.promocao()
gerente.promocao()
print(gerente.__repr__())
print(estagiario1.__repr__())
print(estagiario2.__repr__())




