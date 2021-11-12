class BaseDeDados:
    ### MÉTODO CONSTRUTOR:
    def __init__(self):
        ### O SÍMBOLO DO _ é uma forma de "private" no python ou __ "private" mais forte!!
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

### Instanciando o objeto:
bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Carlos')
### Criando um outro atributo numa nova tentativa de "quebrar" a classe!
bd.__dados = "outra coisa"
# print(bd.__dados)
### valor atributo real:
print(bd._BaseDeDados__dados)
### Listagem acontece normalmente!
bd.lista_clientes()