'''
Propriedades

- Métodos publicos utilizados para manipular atributos/métodos privados.
java : get set
'''
class Celular:
    def __init__(self, data, senha, saldoBanco, msg):
        self.__data = data
        self.__senha = senha
        self.__saldoBanco = saldoBanco
        self.__msg = msg

    ### Indica que esse método é um método publico de manipulação de atributos!
    @property
    def data(self):
        return f'Data de hoje: {self.__data}'

    @property
    def senha(self):
        return self.__senha

    @property
    def saldoBanco(self):
        return self.__saldoBanco

    @property
    def msg(self):
        return self.__msg

    ### Usando um setter em python:
    @msg.setter
    def msg(self, resposta):
        self.__msg = resposta

    @property ### Não se comporta mais como método e sim como propriedade, não precisa dos () para ser chamado no objetos
    def mensagem(self):
        return f'Data: {self.__data}. Mensagem: {self.__msg}'

cel1 = Celular('18/11/2024', 'Mortadela1', 3210, 'Ei sumido(a)!')
cel2 = Celular('09/10/2023', 'Abacate1', 4210, 'Tirou a carne do congelador??')

### Possível acessar esse atributo devido ao método com property:
print(cel1.data)

print(cel1.senha)
print(f'Saldo total: {cel1.saldoBanco + cel2.saldoBanco}')

## Após passar o método setter:
print(cel1.msg)
cel1.msg = 'Olá, como vai?'
print(cel1.smg)

print(cel2.msg)
cel2.msg = 'Esqueci!'
print(cel2.msg)

### MÉTODO COMO PROPRIEDADE: Chamando o "método"/propriedade sem usar os ()
print(cel1.mensagem)
print(cel2.mensagem)



